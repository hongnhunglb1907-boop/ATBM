"""
Views for Books App
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Avg, Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Book, Subject, PurchaseRequest
from .forms import BookForm, BookSearchForm


# ==================== HOME ====================
def home_view(request):
    """Trang chủ - Hiển thị sách mới nhất"""
    latest_books = Book.objects.filter(
        status='available'
    ).select_related('seller__profile', 'subject')[:12]

    # Thống kê
    total_books = Book.objects.filter(status='available').count()
    total_sellers = Book.objects.filter(
        status='available'
    ).values('seller').distinct().count()

    # Lấy danh sách subjects cho search form
    subjects = Subject.objects.all()

    context = {
        'latest_books': latest_books,
        'total_books': total_books,
        'total_sellers': total_sellers,
        'subjects': subjects,
    }
    return render(request, 'home.html', context)


# ==================== BOOK LIST ====================
class BookListView(ListView):
    """Danh sách sách đang bán"""
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 20

    def get_queryset(self):
        queryset = Book.objects.filter(status='available').select_related(
            'seller__profile', 'subject'
        )

        # Search
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # Filter by subject
        subject_id = self.request.GET.get('subject')
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)

        # Filter by condition
        condition = self.request.GET.get('condition')
        if condition:
            queryset = queryset.filter(condition=condition)

        # Filter by price range
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        # Sorting
        sort_by = self.request.GET.get('sort', '-created_at')
        queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['search_form'] = BookSearchForm(self.request.GET)
        return context


# ==================== BOOK DETAIL ====================
class BookDetailView(DetailView):
    """Chi tiết sách"""
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.select_related(
            'seller__profile', 'subject', 'buyer'
        ).prefetch_related('images', 'ratings__reviewer__profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object

        # Tăng view count
        book.increment_view()

        # Sách khác cùng người bán
        context['seller_other_books'] = Book.objects.filter(
            seller=book.seller,
            status='available'
        ).exclude(pk=book.pk)[:4]

        # Sách tương tự (cùng subject)
        if book.subject:
            context['similar_books'] = Book.objects.filter(
                subject=book.subject,
                status='available'
            ).exclude(pk=book.pk)[:4]

        # Lấy purchase request của user hiện tại (nếu đã đăng nhập)
        if self.request.user.is_authenticated and self.request.user != book.seller:
            context['user_purchase_request'] = PurchaseRequest.objects.filter(
                book=book,
                buyer=self.request.user
            ).first()
        else:
            context['user_purchase_request'] = None

        return context


# ==================== CREATE BOOK ====================
class BookCreateView(LoginRequiredMixin, CreateView):
    """Đăng bài bán sách mới"""
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('my_books')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        messages.success(self.request, 'Đăng bài thành công!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Có lỗi trong form. Vui lòng kiểm tra lại.')
        return super().form_invalid(form)


# ==================== UPDATE BOOK ====================
class BookUpdateView(LoginRequiredMixin, UpdateView):
    """Chỉnh sửa bài đăng"""
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html'

    def get_queryset(self):
        return Book.objects.filter(seller=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Cập nhật thành công!')
        return super().form_valid(form)


# ==================== DELETE BOOK ====================
class BookDeleteView(LoginRequiredMixin, DeleteView):
    """Xóa bài đăng"""
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def get_queryset(self):
        return Book.objects.filter(seller=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Đã xóa bài đăng!')
        return super().delete(request, *args, **kwargs)


# ==================== MARK AS SOLD ====================
@login_required
def mark_as_sold(request, pk):
    """Đánh dấu sách đã bán"""
    book = get_object_or_404(Book, pk=pk, seller=request.user)
    book.status = 'sold'
    book.save()
    messages.success(request, f'Đã đánh dấu "{book.title}" là đã bán!')
    return redirect('book_detail', pk=pk)


# ==================== MARK AS AVAILABLE ====================
@login_required
def mark_as_available(request, pk):
    """Đánh dấu sách đang bán (kích hoạt lại)"""
    book = get_object_or_404(Book, pk=pk, seller=request.user)
    book.status = 'available'
    book.save()
    messages.success(request, f'Đã kích hoạt lại "{book.title}"! Sách hiện đang đăng bán.')
    return redirect('book_detail', pk=pk)


# ==================== MY BOOKS ====================
@login_required
def my_books(request):
    """Danh sách sách của tôi"""
    books = Book.objects.filter(
        seller=request.user
    ).select_related('subject', 'buyer').order_by('-created_at')
    
    # Lấy các yêu cầu mua đang chờ duyệt
    pending_requests = PurchaseRequest.objects.filter(
        book__seller=request.user,
        status='pending'
    ).select_related('book', 'buyer__profile').order_by('-created_at')

    context = {
        'books': books,
        'pending_requests': pending_requests,
        'total_count': books.count(),
        'sold_count': books.filter(status='sold').count(),
        'available_count': books.filter(status='available').count(),
    }
    return render(request, 'books/my_books.html', context)


# ==================== PURCHASE REQUEST ====================
@login_required
def create_purchase_request(request, pk):
    """Tạo yêu cầu mua sách - 'Tôi đã mua sách này'"""
    book = get_object_or_404(Book, pk=pk)
    
    # Kiểm tra: Không thể mua chính sách của mình
    if book.seller == request.user:
        messages.error(request, 'Bạn không thể mua chính sách của mình!')
        return redirect('book_detail', pk=pk)
    
    # Kiểm tra: Sách phải đang còn bán
    if not book.is_available:
        messages.error(request, 'Sách này đã bán hoặc không còn bán!')
        return redirect('book_detail', pk=pk)
    
    # Kiểm tra: Đã gửi yêu cầu chưa
    existing_request = PurchaseRequest.objects.filter(
        book=book,
        buyer=request.user
    ).first()
    
    if existing_request:
        if existing_request.status == 'pending':
            messages.warning(request, 'Bạn đã gửi yêu cầu mua sách này rồi. Vui lòng chờ người bán duyệt.')
        elif existing_request.status == 'approved':
            messages.info(request, 'Yêu cầu mua sách này đã được duyệt!')
        else:
            messages.warning(request, 'Yêu cầu mua sách trước đó đã bị từ chối.')
        return redirect('book_detail', pk=pk)
    
    # Tạo yêu cầu mới
    PurchaseRequest.objects.create(
        book=book,
        buyer=request.user,
        status='pending'
    )
    messages.success(request, f'Đã gửi yêu cầu mua sách "{book.title}". Vui lòng chờ người bán duyệt.')
    return redirect('book_detail', pk=pk)


@login_required
def approve_purchase_request(request, request_id):
    """Người bán duyệt yêu cầu mua"""
    purchase_request = get_object_or_404(
        PurchaseRequest,
        pk=request_id,
        book__seller=request.user,
        status='pending'
    )
    
    purchase_request.approve()
    messages.success(
        request,
        f'Đã duyệt yêu cầu mua từ {purchase_request.buyer.username}. '
        f'Sách "{purchase_request.book.title}" đã được đánh dấu là đã bán.'
    )
    return redirect('my_books')


@login_required
def reject_purchase_request(request, request_id):
    """Người bán từ chối yêu cầu mua"""
    purchase_request = get_object_or_404(
        PurchaseRequest,
        pk=request_id,
        book__seller=request.user,
        status='pending'
    )
    
    purchase_request.reject()
    messages.warning(
        request,
        f'Đã từ chối yêu cầu mua từ {purchase_request.buyer.username}.'
    )
    return redirect('my_books')


@login_required
def my_purchase_requests(request):
    """Danh sách yêu cầu mua sách của tôi (người mua)"""
    requests_sent = PurchaseRequest.objects.filter(
        buyer=request.user
    ).select_related('book__seller__profile').order_by('-created_at')

    context = {
        'requests_sent': requests_sent,
        'pending_count': requests_sent.filter(status='pending').count(),
        'approved_count': requests_sent.filter(status='approved').count(),
        'rejected_count': requests_sent.filter(status='rejected').count(),
    }
    return render(request, 'books/my_purchase_requests.html', context)


# ==================== PURCHASED BOOKS ====================
@login_required
def purchased_books(request):
    """
    Trang 'Sách đã mua' - Hiển thị các sách user đã mua
    Chỉ hiển thị Book có status='sold' và buyer=request.user
    """
    from ratings.models import Rating

    # Lấy các sách đã mua: status = SOLD AND buyer = request.user
    purchased_books = Book.objects.filter(
        buyer=request.user,
        status='sold'
    ).select_related(
        'seller__profile',
        'subject'
    ).prefetch_related(
        'ratings__reviewer__profile'
    ).order_by('-updated_at')

    # Annotation để kiểm tra đánh giá
    for book in purchased_books:
        book.has_rated = Rating.objects.filter(
            seller=book.seller,
            reviewer=request.user,
            book=book
        ).exists()

        # Lấy đánh giá nếu có
        if book.has_rated:
            book.user_rating = Rating.objects.filter(
                seller=book.seller,
                reviewer=request.user,
                book=book
            ).first()

    context = {
        'purchased_books': purchased_books,
        'total_count': purchased_books.count(),
    }
    return render(request, 'books/purchased_books.html', context)
