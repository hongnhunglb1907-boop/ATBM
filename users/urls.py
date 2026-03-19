"""
URLs for Users App
"""
from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('dang-ky/', views.RegisterView.as_view(), name='user_register'),
    path('dang-nhap/', views.user_login, name='user_login'),
    path('dang-xuat/', views.user_logout, name='user_logout'),

    # Profile
    path('ho-so/', views.user_profile, name='user_profile'),
    path('ho-so/cap-nhat/', views.edit_profile, name='user_edit_profile'),
    path('ho-so/<str:username>/', views.user_profile, name='user_profile_view'),
    path('doi-mat-khau/', views.change_password, name='user_change_password'),
]
