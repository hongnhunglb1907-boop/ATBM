"""
URLs for Ratings App
"""
from django.urls import path
from . import views

urlpatterns = [
    # Create rating
    path('<int:seller_id>/', views.create_rating, name='create_rating', kwargs={'book_id': None}),
    path('<int:seller_id>/<int:book_id>/', views.create_rating, name='create_rating_for_book'),

    # View ratings
    path('nguoi-dung/<str:username>/', views.user_ratings, name='user_ratings'),
]
