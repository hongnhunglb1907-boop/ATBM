"""
Views for Users App
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import (
    UserRegisterForm,
    UserProfileForm,
    UserUpdateForm,
    ChangePasswordForm
)


# ==================== REGISTER ====================
class RegisterView(CreateView):
    """Đăng ký tài khoản mới"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_register.html'
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Chào mừng {self.object.username}! Đăng ký thành công.'
        )
        return response


# ==================== LOGIN ====================
def user_login(request):
    """Đăng nhập"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Chào mừng trở lại, {user.username}!')

            # Redirect sau khi login
            next_url = request.GET.get('next', reverse_lazy('home'))
            return redirect(next_url)
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
    else:
        form = AuthenticationForm()

    return render(request, 'users/user_login.html', {'form': form})


# ==================== LOGOUT ====================
def user_logout(request):
    """Đăng xuất"""
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất!')
    return redirect('home')


# ==================== PROFILE ====================
@login_required
def user_profile(request, username=None):
    """Hồ sơ người dùng"""
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user

    profile = user.profile
    books = user.books_for_sale.select_related('subject').all()[:6]

    # Lấy đánh giá
    from ratings.models import Rating
    ratings = Rating.objects.filter(seller=user).select_related(
        'reviewer__profile', 'book'
    ).order_by('-created_at')[:10]

    context = {
        'profile_user': user,
        'profile': profile,
        'books': books,
        'ratings': ratings,
    }
    return render(request, 'users/user_profile.html', context)


# ==================== EDIT PROFILE ====================
@login_required
def edit_profile(request):
    """Chỉnh sửa hồ sơ"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Cập nhật hồ sơ thành công!')
            return redirect('user_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/user_edit_profile.html', context)


# ==================== CHANGE PASSWORD ====================
@login_required
def change_password(request):
    """Đổi mật khẩu"""
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')

            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Đổi mật khẩu thành công!')
                return redirect('user_login')
            else:
                messages.error(request, 'Mật khẩu cũ không đúng!')
    else:
        form = ChangePasswordForm()

    return render(request, 'users/user_change_password.html', {'form': form})
