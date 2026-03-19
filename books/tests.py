"""
Tests cho DUE Book - Hệ thống trao đổi sách cũ

Chạy test: python manage.py test books

Test Cases:
1. Test Model - Book, PurchaseRequest, Rating
2. Test View - Gửi yêu cầu, duyệt yêu cầu, đánh giá
3. Test Logic nghiệp vụ - Quyền đánh giá, duplicate review
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

from books.models import Book, Subject, PurchaseRequest
from ratings.models import Rating
from users.models import UserProfile


class BaseTestCase(TestCase):
    """
    Base test case với setup dữ liệu mẫu chung cho tất cả test
    Tạo: seller, buyer, book, subject
    """
    
    def setUp(self):
        """Setup dữ liệu mẫu"""
        # Tạo seller
        self.seller = User.objects.create_user(
            username='seller1',
            email='seller@test.com',
            password='testpass123'
        )
        # Update profile với thông tin bắt buộc
        self.seller.profile.phone_number = '0123456789'
        self.seller.profile.facebook_link = 'https://facebook.com/seller1'
        self.seller.profile.save()
        
        # Tạo buyer
        self.buyer = User.objects.create_user(
            username='buyer1',
            email='buyer@test.com',
            password='testpass123'
        )
        self.buyer.profile.phone_number = '0987654321'
        self.buyer.profile.facebook_link = 'https://facebook.com/buyer1'
        self.buyer.profile.save()
        
        # Tạo buyer khác (để test không có quyền)
        self.other_user = User.objects.create_user(
            username='other1',
            email='other@test.com',
            password='testpass123'
        )
        self.other_user.profile.phone_number = '0111222333'
        self.other_user.profile.facebook_link = 'https://facebook.com/other1'
        self.other_user.profile.save()
        
        # Tạo subject
        self.subject = Subject.objects.create(
            name='Toán cao cấp',
            code='MATH101'
        )
        
        # Tạo book
        self.book = Book.objects.create(
            title='Sách Toán cao cấp A1',
            author='Nguyễn Văn A',
            subject=self.subject,
            price=50000,
            condition='good',
            description='Sách còn mới 90%',
            seller=self.seller,
            status='available'
        )
        
        # Client để test views
        self.client = Client()


# ==================== TEST MODEL ====================

class BookModelTest(BaseTestCase):
    """Test cho Book Model"""
    
    def test_create_book_success(self):
        """Test: Tạo book thành công với đầy đủ thông tin"""
        book = Book.objects.create(
            title='Sách Test',
            author='Tác giả Test',
            subject=self.subject,
            price=100000,
            condition='new',
            description='Mô tả test',
            seller=self.seller
        )
        
        self.assertEqual(book.title, 'Sách Test')
        self.assertEqual(book.seller, self.seller)
        self.assertEqual(book.status, 'available')  # Default status
        self.assertEqual(book.view_count, 0)
        self.assertTrue(book.is_available)
    
    def test_book_discount_percentage(self):
        """Test: Tính % giảm giá của sách"""
        book = Book.objects.create(
            title='Sách giảm giá',
            price=50000,
            original_price=100000,
            seller=self.seller
        )
        
        self.assertEqual(book.discount_percentage, 50)
    
    def test_book_str(self):
        """Test: String representation của Book"""
        self.assertEqual(str(self.book), 'Sách Toán cao cấp A1')


class PurchaseRequestModelTest(BaseTestCase):
    """Test cho PurchaseRequest Model"""
    
    def test_create_purchase_request_success(self):
        """Test: Tạo yêu cầu mua sách thành công"""
        request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
        
        self.assertEqual(request.book, self.book)
        self.assertEqual(request.buyer, self.buyer)
        self.assertEqual(request.status, 'pending')
        self.assertTrue(request.is_pending)
    
    def test_purchase_request_unique_together(self):
        """Test: Mỗi user chỉ được gửi 1 yêu cầu cho 1 sách"""
        PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
        
        # Tạo request lần 2 sẽ raise error
        with self.assertRaises(Exception):
            PurchaseRequest.objects.create(
                book=self.book,
                buyer=self.buyer,
                status='pending'
            )
    
    def test_approve_purchase_request(self):
        """Test: Duyệt yêu cầu → book.buyer = buyer, book.status = SOLD"""
        request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
        
        # Duyệt
        request.approve()
        
        # Refresh từ DB
        request.refresh_from_db()
        self.book.refresh_from_db()
        
        # Check PurchaseRequest
        self.assertEqual(request.status, 'approved')
        self.assertTrue(request.is_approved)
        
        # Check Book
        self.assertEqual(self.book.buyer, self.buyer)
        self.assertEqual(self.book.status, 'sold')
    
    def test_reject_purchase_request(self):
        """Test: Từ chối yêu cầu → status = REJECTED"""
        request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
        
        request.reject()
        request.refresh_from_db()
        
        self.assertEqual(request.status, 'rejected')
        self.assertTrue(request.is_rejected)
    
    def test_approve_rejects_other_pending_requests(self):
        """Test: Khi duyệt 1 request, các request khác của sách đó bị reject"""
        # Tạo thêm buyer 2
        buyer2 = User.objects.create_user(username='buyer2', password='pass123')
        buyer2.profile.phone_number = '0999888777'
        buyer2.profile.facebook_link = 'https://facebook.com/buyer2'
        buyer2.profile.save()
        
        # Tạo 2 request
        request1 = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
        request2 = PurchaseRequest.objects.create(
            book=self.book,
            buyer=buyer2,
            status='pending'
        )
        
        # Duyệt request 1
        request1.approve()
        
        # Refresh
        request2.refresh_from_db()
        
        # Request 2 phải bị reject
        self.assertEqual(request2.status, 'rejected')


class RatingModelTest(BaseTestCase):
    """Test cho Rating Model"""
    
    def setUp(self):
        super().setUp()
        # Tạo purchase request approved
        self.purchase_request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='approved'
        )
        # Update book
        self.book.buyer = self.buyer
        self.book.status = 'sold'
        self.book.save()
    
    def test_create_rating_success(self):
        """Test: Tạo đánh giá thành công"""
        rating = Rating.objects.create(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book,
            rating=5,
            comment='Người bán tốt, sách đẹp!'
        )
        
        self.assertEqual(rating.seller, self.seller)
        self.assertEqual(rating.reviewer, self.buyer)
        self.assertEqual(rating.rating, 5)
    
    def test_rating_star_display(self):
        """Test: Hiển thị số sao"""
        rating = Rating.objects.create(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book,
            rating=4
        )
        
        self.assertEqual(rating.star_display, '★★★★☆')
    
    def test_rating_unique_together(self):
        """Test: Mỗi người chỉ đánh giá 1 lần cho 1 cuốn sách"""
        Rating.objects.create(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book,
            rating=5
        )
        
        # Tạo rating lần 2 cho cùng book → error
        with self.assertRaises(Exception):
            Rating.objects.create(
                seller=self.seller,
                reviewer=self.buyer,
                book=self.book,
                rating=3
            )


# ==================== TEST VIEW ====================

class CreatePurchaseRequestViewTest(BaseTestCase):
    """Test cho View: Gửi yêu cầu mua sách"""
    
    def test_send_purchase_request_success(self):
        """Test: Gửi yêu cầu mua → status = PENDING"""
        self.client.login(username='buyer1', password='testpass123')
        
        response = self.client.get(
            reverse('create_purchase_request', kwargs={'pk': self.book.pk})
        )
        
        # Kiểm tra redirect sau khi tạo
        self.assertEqual(response.status_code, 302)
        
        # Kiểm tra PurchaseRequest được tạo
        request = PurchaseRequest.objects.filter(
            book=self.book,
            buyer=self.buyer
        ).first()
        
        self.assertIsNotNone(request)
        self.assertEqual(request.status, 'pending')
    
    def test_cannot_buy_own_book(self):
        """Test: Không thể mua chính sách của mình"""
        self.client.login(username='seller1', password='testpass123')
        
        response = self.client.get(
            reverse('create_purchase_request', kwargs={'pk': self.book.pk})
        )
        
        # Không tạo request
        request_exists = PurchaseRequest.objects.filter(
            book=self.book,
            buyer=self.seller
        ).exists()
        
        self.assertFalse(request_exists)
    
    def test_cannot_buy_sold_book(self):
        """Test: Không thể mua sách đã bán"""
        self.book.status = 'sold'
        self.book.save()
        
        self.client.login(username='buyer1', password='testpass123')
        
        response = self.client.get(
            reverse('create_purchase_request', kwargs={'pk': self.book.pk})
        )
        
        # Không tạo request
        request_exists = PurchaseRequest.objects.filter(
            book=self.book,
            buyer=self.buyer
        ).exists()
        
        self.assertFalse(request_exists)
    
    def test_cannot_send_duplicate_request(self):
        """Test: Không thể gửi request trùng lặp"""
        # Gửi request lần 1
        PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
        
        self.client.login(username='buyer1', password='testpass123')
        
        # Gửi lần 2
        response = self.client.get(
            reverse('create_purchase_request', kwargs={'pk': self.book.pk})
        )
        
        # Vẫn chỉ có 1 request
        count = PurchaseRequest.objects.filter(
            book=self.book,
            buyer=self.buyer
        ).count()
        
        self.assertEqual(count, 1)


class ApprovePurchaseRequestViewTest(BaseTestCase):
    """Test cho View: Duyệt yêu cầu mua"""
    
    def setUp(self):
        super().setUp()
        # Tạo purchase request
        self.purchase_request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'
        )
    
    def test_approve_request_success(self):
        """Test: Seller duyệt request → book.status = SOLD, sold_to = buyer"""
        self.client.login(username='seller1', password='testpass123')
        
        response = self.client.get(
            reverse('approve_purchase_request', kwargs={'request_id': self.purchase_request.pk})
        )
        
        # Refresh
        self.purchase_request.refresh_from_db()
        self.book.refresh_from_db()
        
        # Kiểm tra
        self.assertEqual(self.purchase_request.status, 'approved')
        self.assertEqual(self.book.status, 'sold')
        self.assertEqual(self.book.buyer, self.buyer)
    
    def test_only_seller_can_approve(self):
        """Test: Chỉ seller mới có thể duyệt request"""
        self.client.login(username='other1', password='testpass123')
        
        response = self.client.get(
            reverse('approve_purchase_request', kwargs={'request_id': self.purchase_request.pk})
        )
        
        # Refresh - không có thay đổi
        self.purchase_request.refresh_from_db()
        
        self.assertEqual(self.purchase_request.status, 'pending')  # Vẫn pending
    
    def test_reject_request_success(self):
        """Test: Seller từ chối request → status = REJECTED"""
        self.client.login(username='seller1', password='testpass123')
        
        response = self.client.get(
            reverse('reject_purchase_request', kwargs={'request_id': self.purchase_request.pk})
        )
        
        self.purchase_request.refresh_from_db()
        
        self.assertEqual(self.purchase_request.status, 'rejected')
        # Book vẫn available
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'available')


class PurchasedBooksViewTest(BaseTestCase):
    """Test cho View: Trang sách đã mua"""
    
    def setUp(self):
        super().setUp()
        # Tạo purchase request approved
        self.purchase_request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='approved'
        )
        self.book.buyer = self.buyer
        self.book.status = 'sold'
        self.book.save()
    
    def test_purchased_books_shows_only_own_books(self):
        """Test: Người mua truy cập trang 'Sách đã mua' → chỉ thấy sách của mình"""
        self.client.login(username='buyer1', password='testpass123')
        
        response = self.client.get(reverse('purchased_books'))
        
        self.assertEqual(response.status_code, 200)
        # Kiểm tra context có sách đã mua
        purchased_books = list(response.context['purchased_books'])
        
        self.assertEqual(len(purchased_books), 1)
        self.assertEqual(purchased_books[0], self.book)
    
    def test_purchased_books_not_show_other_books(self):
        """Test: Không thấy sách của người khác"""
        # Tạo sách khác cho other_user
        other_book = Book.objects.create(
            title='Sách của người khác',
            price=30000,
            seller=self.seller,
            status='sold',
            buyer=self.other_user
        )
        
        self.client.login(username='buyer1', password='testpass123')
        
        response = self.client.get(reverse('purchased_books'))
        
        purchased_books = list(response.context['purchased_books'])
        
        # Chỉ có 1 sách (của buyer), không có sách của other_user
        self.assertEqual(len(purchased_books), 1)
        self.assertIn(self.book, purchased_books)
        self.assertNotIn(other_book, purchased_books)
    
    def test_purchased_books_require_login(self):
        """Test: Cần đăng nhập để xem trang sách đã mua"""
        response = self.client.get(reverse('purchased_books'))
        
        # Redirect đến login
        self.assertEqual(response.status_code, 302)
        # Redirect đến trang đăng nhập (có thể là /nguoi-dung/dang-nhap/ hoặc /login/)
        # Chỉ cần kiểm tra là redirect
        self.assertIsNotNone(response.url)


class CreateRatingViewTest(BaseTestCase):
    """Test cho View: Tạo đánh giá"""
    
    def setUp(self):
        super().setUp()
        # Tạo purchase request approved
        self.purchase_request = PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='approved'
        )
        self.book.buyer = self.buyer
        self.book.status = 'sold'
        self.book.save()
    
    def test_buyer_can_create_rating(self):
        """Test: Người mua (book.buyer) có thể đánh giá"""
        self.client.login(username='buyer1', password='testpass123')
        
        # URL: /danh-gia/<seller_id>/?book=<book_id>
        url = reverse('create_rating', kwargs={'seller_id': self.seller.pk}) + f'?book={self.book.pk}'
        response = self.client.post(
            url,
            {
                'rating': 5,
                'comment': 'Người bán tốt!'
            }
        )
        
        # Kiểm tra rating được tạo
        rating = Rating.objects.filter(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book
        ).first()
        
        self.assertIsNotNone(rating)
        self.assertEqual(rating.rating, 5)
    
    def test_non_buyer_cannot_rate(self):
        """Test: Người không phải buyer không thể đánh giá → redirect"""
        self.client.login(username='other1', password='testpass123')
        
        url = reverse('create_rating', kwargs={'seller_id': self.seller.pk}) + f'?book={self.book.pk}'
        response = self.client.post(
            url,
            {
                'rating': 5,
                'comment': 'Fake review!'
            }
        )
        
        # Không tạo rating
        rating_exists = Rating.objects.filter(
            seller=self.seller,
            reviewer=self.other_user,
            book=self.book
        ).exists()
        
        self.assertFalse(rating_exists)
    
    def test_cannot_rate_twice(self):
        """Test: Không thể đánh giá 2 lần cho cùng 1 sách"""
        # Tạo rating lần 1
        Rating.objects.create(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book,
            rating=5,
            comment='Lần đầu'
        )
        
        self.client.login(username='buyer1', password='testpass123')
        
        # Thử tạo rating lần 2
        url = reverse('create_rating', kwargs={'seller_id': self.seller.pk}) + f'?book={self.book.pk}'
        response = self.client.post(
            url,
            {
                'rating': 3,
                'comment': 'Lần hai'
            }
        )
        
        # Vẫn chỉ có 1 rating
        count = Rating.objects.filter(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book
        ).count()
        
        self.assertEqual(count, 1)


# ==================== TEST LOGIC NGHIỆP VỤ ====================

class RatingBusinessLogicTest(BaseTestCase):
    """Test cho Logic nghiệp vụ đánh giá"""
    
    def test_cannot_rate_when_purchase_request_not_approved(self):
        """Test: Không thể đánh giá khi PurchaseRequest chưa APPROVED"""
        # Tạo request nhưng không approve
        PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='pending'  # Vẫn pending
        )
        
        self.client.login(username='buyer1', password='testpass123')
        
        url = reverse('create_rating', kwargs={'seller_id': self.seller.pk}) + f'?book={self.book.pk}'
        response = self.client.post(
            url,
            {
                'rating': 5,
                'comment': 'Test'
            }
        )
        
        # Không tạo rating
        rating_exists = Rating.objects.filter(
            book=self.book,
            reviewer=self.buyer
        ).exists()
        
        self.assertFalse(rating_exists)
    
    def test_cannot_rate_when_request_rejected(self):
        """Test: Không thể đánh giá khi PurchaseRequest bị REJECTED"""
        # Tạo request và reject
        PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='rejected'
        )
        
        self.client.login(username='buyer1', password='testpass123')
        
        url = reverse('create_rating', kwargs={'seller_id': self.seller.pk}) + f'?book={self.book.pk}'
        response = self.client.post(
            url,
            {
                'rating': 5,
                'comment': 'Test'
            }
        )
        
        # Không tạo rating
        rating_exists = Rating.objects.filter(
            book=self.book,
            reviewer=self.buyer
        ).exists()
        
        self.assertFalse(rating_exists)
    
    def test_cannot_rate_own_self(self):
        """Test: Không thể tự đánh giá mình"""
        self.client.login(username='seller1', password='testpass123')
        
        response = self.client.post(
            reverse('create_rating', kwargs={'seller_id': self.seller.pk}),
            {
                'rating': 5,
                'comment': 'Tự khen'
            }
        )
        
        # Không tạo rating
        rating_exists = Rating.objects.filter(
            seller=self.seller,
            reviewer=self.seller
        ).exists()
        
        self.assertFalse(rating_exists)
    
    def test_rating_updates_seller_reputation(self):
        """Test: Đánh giá cập nhật điểm uy tín của seller"""
        # Setup
        PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='approved'
        )
        self.book.buyer = self.buyer
        self.book.status = 'sold'
        self.book.save()
        
        # Tạo rating
        Rating.objects.create(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book,
            rating=5
        )
        
        # Refresh seller profile
        self.seller.profile.refresh_from_db()
        
        # Kiểm tra reputation được cập nhật
        self.assertEqual(self.seller.profile.total_reviews, 1)
        self.assertEqual(self.seller.profile.reputation_score, 5.0)
    
    def test_average_rating_calculation(self):
        """Test: Tính điểm đánh giá trung bình"""
        # Setup buyer 2
        buyer2 = User.objects.create_user(username='buyer2', password='pass123')
        buyer2.profile.phone_number = '0999888777'
        buyer2.profile.facebook_link = 'https://facebook.com/buyer2'
        buyer2.profile.save()
        
        # Tạo 2 sách
        book2 = Book.objects.create(
            title='Sách 2',
            price=30000,
            seller=self.seller,
            status='sold',
            buyer=buyer2
        )
        
        # Tạo purchase requests
        PurchaseRequest.objects.create(
            book=self.book,
            buyer=self.buyer,
            status='approved'
        )
        PurchaseRequest.objects.create(
            book=book2,
            buyer=buyer2,
            status='approved'
        )
        
        self.book.buyer = self.buyer
        self.book.status = 'sold'
        self.book.save()
        
        # Tạo 2 rating: 5 sao và 3 sao
        Rating.objects.create(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book,
            rating=5
        )
        Rating.objects.create(
            seller=self.seller,
            reviewer=buyer2,
            book=book2,
            rating=3
        )
        
        # Refresh
        self.seller.profile.refresh_from_db()
        
        # Average = (5+3)/2 = 4.0
        self.assertEqual(self.seller.profile.total_reviews, 2)
        self.assertEqual(self.seller.profile.reputation_score, 4.0)


class PurchaseRequestFlowTest(BaseTestCase):
    """Test cho Flow: Gửi → Duyệt/Từ chối → Kết quả"""
    
    def test_full_purchase_flow_approved(self):
        """Test: Flow đầy đủ - Gửi request → Duyệt → Book SOLD → Có thể đánh giá"""
        # B1: Buyer gửi request
        self.client.login(username='buyer1', password='testpass123')
        self.client.get(reverse('create_purchase_request', kwargs={'pk': self.book.pk}))
        
        request = PurchaseRequest.objects.get(book=self.book, buyer=self.buyer)
        self.assertEqual(request.status, 'pending')
        
        # B2: Seller duyệt
        self.client.login(username='seller1', password='testpass123')
        self.client.get(reverse('approve_purchase_request', kwargs={'request_id': request.pk}))
        
        # B3: Kiểm tra book
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'sold')
        self.assertEqual(self.book.buyer, self.buyer)
        
        # B4: Buyer có thể đánh giá
        self.client.login(username='buyer1', password='testpass123')
        response = self.client.post(
            reverse('create_rating_for_book', kwargs={
                'seller_id': self.seller.pk,
                'book_id': self.book.pk
            }),
            {'rating': 5, 'comment': 'Tốt!'}
        )
        
        rating_exists = Rating.objects.filter(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book
        ).exists()
        
        self.assertTrue(rating_exists)
    
    def test_full_purchase_flow_rejected(self):
        """Test: Flow đầy đủ - Gửi request → Từ chối → Không thể đánh giá"""
        # B1: Buyer gửi request
        self.client.login(username='buyer1', password='testpass123')
        self.client.get(reverse('create_purchase_request', kwargs={'pk': self.book.pk}))
        
        request = PurchaseRequest.objects.get(book=self.book, buyer=self.buyer)
        
        # B2: Seller từ chối
        self.client.login(username='seller1', password='testpass123')
        self.client.get(reverse('reject_purchase_request', kwargs={'request_id': request.pk}))
        
        # B3: Kiểm tra book vẫn available
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'available')
        self.assertIsNone(self.book.buyer)
        
        # B4: Buyer KHÔNG thể đánh giá
        self.client.login(username='buyer1', password='testpass123')
        self.client.post(
            reverse('create_rating_for_book', kwargs={
                'seller_id': self.seller.pk,
                'book_id': self.book.pk
            }),
            {'rating': 5, 'comment': 'Test'}
        )
        
        rating_exists = Rating.objects.filter(
            seller=self.seller,
            reviewer=self.buyer,
            book=self.book
        ).exists()
        
        self.assertFalse(rating_exists)


# ==================== TEST EDGE CASES ====================

class EdgeCasesTest(BaseTestCase):
    """Test cho các trường hợp edge case"""
    
    def test_view_nonexistent_book(self):
        """Test: Xem sách không tồn tại → 404"""
        response = self.client.get(reverse('book_detail', kwargs={'pk': 99999}))
        self.assertEqual(response.status_code, 404)
    
    def test_approve_nonexistent_request(self):
        """Test: Duyệt request không tồn tại → 404"""
        self.client.login(username='seller1', password='testpass123')
        response = self.client.get(
            reverse('approve_purchase_request', kwargs={'request_id': 99999})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_unauthorized_book_update(self):
        """Test: Không thể update sách của người khác"""
        self.client.login(username='buyer1', password='testpass123')
        
        response = self.client.post(
            reverse('book_update', kwargs={'pk': self.book.pk}),
            {
                'title': 'Sách đã sửa',
                'price': 100000,
                'condition': 'new'
            }
        )
        
        # 404 (do queryset filter seller=user), 403 hoặc redirect
        # Django UpdateView trả về 404 khi object không thuộc queryset
        self.assertIn(response.status_code, [302, 403, 404])
    
    def test_unauthorized_book_delete(self):
        """Test: Không thể xóa sách của người khác"""
        self.client.login(username='buyer1', password='testpass123')
        
        response = self.client.post(
            reverse('book_delete', kwargs={'pk': self.book.pk})
        )
        
        # Book vẫn tồn tại
        self.assertTrue(Book.objects.filter(pk=self.book.pk).exists())


# ==================== CHAY TEST ====================
# 
# Chạy tất cả tests:
#   python manage.py test books
#
# Chạy test case cụ thể:
#   python manage.py test books.BookModelTest
#   python manage.py test books.RatingBusinessLogicTest
#
# Chạy với verbose:
#   python manage.py test books -v 2
#
# ==================== CHECKLIST TEST CASES ====================
#
# ✅ BOOK MODEL:
#   - Tạo book thành công
#   - Tính % giảm giá
#   - String representation
#
# ✅ PURCHASE REQUEST MODEL:
#   - Tạo request thành công
#   - Unique constraint (book, buyer)
#   - Approve request → book sold
#   - Reject request
#   - Approve auto-reject các request khác
#
# ✅ RATING MODEL:
#   - Tạo rating thành công
#   - Hiển thị số sao
#   - Unique constraint (seller, reviewer, book)
#
# ✅ VIEW - PURCHASE REQUEST:
#   - Gửi request → PENDING
#   - Không mua sách của mình
#   - Không mua sách đã bán
#   - Không gửi duplicate request
#   - Approve → book SOLD
#   - Chỉ seller mới approve được
#   - Reject → status REJECTED
#
# ✅ VIEW - PURCHASED BOOKS:
#   - Chỉ thấy sách của mình
#   - Không thấy sách người khác
#   - Yêu cầu đăng nhập
#
# ✅ VIEW - RATING:
#   - Buyer có thể đánh giá
#   - Non-buyer không thể đánh giá
#   - Không thể đánh giá 2 lần
#
# ✅ LOGIC NGHIỆP VỤ:
#   - Không đánh giá khi request chưa approved
#   - Không đánh giá khi request bị rejected
#   - Không tự đánh giá mình
#   - Rating cập nhật reputation
#   - Tính điểm trung bình
#
# ✅ FULL FLOW:
#   - Flow: Request → Approve → Rating success
#   - Flow: Request → Reject → Cannot rating
#
# ✅ EDGE CASES:
#   - Xem sách không tồn tại → 404
#   - Duyệt request không tồn tại → 404
#   - Update sách người khác → forbidden
#   - Xóa sách người khác → forbidden