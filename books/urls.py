"""
URLs for Books App
"""
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home_view, name='home'),

    # Books
    path('sach/', views.BookListView.as_view(), name='book_list'),
    path('sach/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('dang-ban-sach/', views.BookCreateView.as_view(), name='book_create'),
    path('sach/<int:pk>/sua/', views.BookUpdateView.as_view(), name='book_update'),
    path('sach/<int:pk>/xoa/', views.BookDeleteView.as_view(), name='book_delete'),
    path('sach/<int:pk>/da-ban/', views.mark_as_sold, name='book_mark_sold'),
    path('sach/<int:pk>/kich-hoat/', views.mark_as_available, name='book_mark_available'),

    # My Books
    path('sach-cua-toi/', views.my_books, name='my_books'),

    # Purchased Books
    path('sach-da-mua/', views.purchased_books, name='purchased_books'),
    
    # Purchase Request
    path('sach/<int:pk>/yeu-cau-mua/', views.create_purchase_request, name='create_purchase_request'),
    path('yeu-cau-mua/<int:request_id>/duyet/', views.approve_purchase_request, name='approve_purchase_request'),
    path('yeu-cau-mua/<int:request_id>/tu-choi/', views.reject_purchase_request, name='reject_purchase_request'),
    path('yeu-cau-mua-cua-toi/', views.my_purchase_requests, name='my_purchase_requests'),
]
