"""
Views for Ratings App
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.db.models import Avg

from .models import Rating
from .forms import RatingForm


# ==================== CREATE RATING ====================
@login_required
def create_rating(request, seller_id, book_id=None):
    """Tạo đánh giá người bán - Chỉ cho buyer đã được duyệt"""
    from books.models import Book, PurchaseRequest
    
    seller = get_object_or_404(User, pk=seller_id)

    # Check không được tự đánh giá mình
    if seller == request.user:
        messages.error(request, 'Bạn không thể tự đánh giá mình!')
        return redirect('home')

    # Lấy book từ tham số URL hoặc query param
    if book_id is None:
        book_id = request.GET.get('book')
    book = None
    if book_id:
        book = get_object_or_404(Book, pk=book_id)

    # KIỂMTRA QUYỀN: Chỉ buyer đã được duyệt mới được đánh giá
    if book:
        # Kiểm tra sách đã bán chưa
        if book.status != 'sold':
            messages.error(request, 'Sách này chưa được đánh dấu là đã bán!')
            return redirect('book_detail', pk=book.pk)
        
        # Kiểm tra user hiện tại có phải là buyer không
        if book.buyer != request.user:
            messages.error(request, 'Chỉ người mua đã được xác nhận mới có thể đánh giá!')
            return redirect('book_detail', pk=book.pk)
        
        # Kiểm tra PurchaseRequest đã được duyệt
        approved_request = PurchaseRequest.objects.filter(
            book=book,
            buyer=request.user,
            status='approved'
        ).exists()
        
        if not approved_request:
            messages.error(request, 'Bạn cần được người bán xác nhận giao dịch trước khi đánh giá!')
            return redirect('book_detail', pk=book.pk)
    else:
        # Nếu không có book, cần kiểm tra xem user có phải đã mua sách nào của seller không
        approved_purchases = PurchaseRequest.objects.filter(
            book__seller=seller,
            buyer=request.user,
            status='approved'
        ).exists()
        
        if not approved_purchases:
            messages.error(request, 'Bạn chỉ có thể đánh giá sau khi mua sách từ người bán này!')
            return redirect('user_profile_view', username=seller.username)

    # Check đã đánh giá chưa
    existing_rating = Rating.objects.filter(
        seller=seller,
        reviewer=request.user,
        book=book
    ).first()

    if existing_rating:
        messages.warning(request, 'Bạn đã đánh giá người bán này rồi!')
        return redirect('book_detail', pk=book.pk) if book else redirect('home')

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.seller = seller
            rating.reviewer = request.user
            rating.book = book
            rating.save()
            messages.success(request, 'Đánh giá thành công!')
            return redirect('user_profile_view', username=seller.username)
    else:
        form = RatingForm()

    context = {
        'form': form,
        'seller': seller,
        'book': book,
    }
    return render(request, 'ratings/rating_create.html', context)


# ==================== USER RATINGS LIST ====================
def user_ratings(request, username):
    """Danh sách đánh giá của một user"""
    user = get_object_or_404(User, username=username)

    ratings = Rating.objects.filter(
        seller=user
    ).select_related('reviewer__profile', 'book').order_by('-created_at')

    # Thống kê
    avg_rating = ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    rating_counts = {}
    for i in range(1, 6):
        rating_counts[i] = ratings.filter(rating=i).count()

    context = {
        'profile_user': user,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'rating_counts': rating_counts,
    }
    return render(request, 'ratings/rating_list.html', context)
