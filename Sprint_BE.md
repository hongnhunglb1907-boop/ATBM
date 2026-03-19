# Sprint Backend: Chức năng Đăng nhập (Login)

## 📋 Thông tin Sprint

| Thông tin | Chi tiết |
|-----------|----------|
| **Sprint Name** | Backend Login |
| **Mục tiêu** | Hoàn thành xử lý đăng nhập phía server |
| **Thời gian** | 1-2 ngày |
| **Yêu cầu trước** | Đã hoàn thành Front-end Login |

---

## ⚡ HƯỚNG DẪN NHANH (4 BƯỚC)

### 📄 Bước 1: Chỉnh sửa `users/views.py`

Thêm function `user_login` để xử lý đăng nhập.

### 📄 Bước 2: Chỉnh sửa `users/urls.py`

Thêm route cho trang đăng nhập.

### 📄 Bước 3: Kiểm tra `due_book/urls.py`

Đảm bảo đã include `users.urls`.

### 📄 Bước 4: Cấu hình `due_book/settings.py`

Thêm cấu hình `LOGIN_URL` và `LOGIN_REDIRECT_URL`.

---

## ✅ KẾT QUẢ SAU KHI HOÀN THÀNH

```
✅ User có thể đăng nhập với username/password
✅ Session được tạo sau khi đăng nhập
✅ Redirect về trang chủ sau khi đăng nhập
✅ Hiển thị lỗi khi đăng nhập thất bại
```

---

## 1. 🎯 Sprint Goal

Hoàn thành **xử lý Backend** cho chức năng **Đăng nhập**:

- ✅ Nhận và xử lý POST request từ form login
- ✅ Xác thực người dùng (authenticate)
- ✅ Tạo session cho user đã đăng nhập (login)
- ✅ Redirect sau khi đăng nhập thành công
- ✅ Hiển thị lỗi khi đăng nhập thất bại
- ✅ Hỗ trợ tính năng "Remember Me" (tùy chọn)

---

## 2. 📊 Phân tích cách Django xử lý Login

### 2.1 Các hàm chính trong Django Authentication

| Hàm | Module | Mô tả |
|-----|--------|-------|
| `authenticate()` | `django.contrib.auth` | Kiểm tra username/password có đúng không |
| `login()` | `django.contrib.auth` | Tạo session cho user đã xác thực |
| `logout()` | `django.contrib.auth` | Xóa session, đăng xuất user |
| `AuthenticationForm` | `django.contrib.auth.forms` | Form đăng nhập có sẵn của Django |

### 2.2 Flow xử lý authenticate() và login()

```python
# Bước 1: Import các hàm cần thiết
from django.contrib.auth import authenticate, login

# Bước 2: Authenticate - Kiểm tra username/password
user = authenticate(request, username=username, password=password)

# Bước 3: Kiểm tra kết quả
if user is not None:
    # User tồn tại và password đúng
    login(request, user)  # Tạo session
    # Redirect đến trang thành công
else:
    # Đăng nhập thất bại
    # Hiển thị lỗi
```

### 2.3 Cách Django lưu Session

```
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO SESSION FLOW                       │
└─────────────────────────────────────────────────────────────┘

1. User đăng nhập thành công
          │
          ▼
2. Django tạo Session trong database
   ┌─────────────────────────────────┐
   │ django_sessions table           │
   │ - session_key (sessionid)       │
   │ - session_data (encrypted)      │
   │ - expire_date                   │
   └─────────────────────────────────┘
          │
          ▼
3. Django gửi cookie `sessionid` đến browser
   Set-Cookie: sessionid=xxxxx
          │
          ▼
4. Browser lưu cookie và gửi kèm mỗi request
   Cookie: sessionid=xxxxx
          │
          ▼
5. Django đọc sessionid → lấy user → request.user
```

### 2.4 request.user là gì?

```python
# Sau khi login, Django tự động gán user vào request
# Trong view hoặc template:

if request.user.is_authenticated:
    # User đã đăng nhập
    username = request.user.username
    email = request.user.email
else:
    # User chưa đăng nhập (AnonymousUser)
    pass

# Trong template:
# {% if user.is_authenticated %}
#     Xin chào, {{ user.username }}
# {% endif %}
```

---

## 3. 💻 Hướng dẫn chỉnh sửa các file

### 3.1 Chỉnh sửa `users/views.py`

**Mở file:** `users/views.py`

**Thêm code sau vào đầu file (nếu chưa có):**

```python
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
```

**Thêm function `user_login`:**

```python
# ==================== LOGIN ====================
def user_login(request):
    """
    Xử lý đăng nhập người dùng
    
    Flow:
    1. Nếu là GET request → Hiển thị form login
    2. Nếu là POST request → Xử lý đăng nhập
       - Validate form
       - Authenticate user
       - Login nếu hợp lệ
       - Redirect đến trang chủ hoặc trang 'next'
    """
    if request.method == 'POST':
        # Tạo form với dữ liệu từ request
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # Lấy user đã được xác thực
            user = form.get_user()
            
            # Tạo session cho user
            login(request, user)
            
            # Hiển thị thông báo thành công
            messages.success(request, f'Chào mừng trở lại, {user.username}!')
            
            # Redirect đến trang 'next' hoặc trang chủ
            next_url = request.GET.get('next', reverse_lazy('home'))
            return redirect(next_url)
        else:
            # Form không hợp lệ - hiển thị lỗi
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
    else:
        # GET request - tạo form rỗng
        form = AuthenticationForm()

    # Render template với form
    return render(request, 'users/user_login.html', {'form': form})
```

**📄 Code hoàn chỉnh của `users/views.py` (chỉ phần login):**

```python
"""
Views for Users App
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy


# ==================== LOGIN ====================
def user_login(request):
    """Xử lý đăng nhập người dùng"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Chào mừng trở lại, {user.username}!')
            
            # Redirect đến trang 'next' hoặc trang chủ
            next_url = request.GET.get('next', reverse_lazy('home'))
            return redirect(next_url)
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
    else:
        form = AuthenticationForm()

    return render(request, 'users/user_login.html', {'form': form})
```

---

### 3.2 Chỉnh sửa `users/urls.py`

**Mở file:** `users/urls.py`

**Thêm route cho login:**

```python
"""
URL routes for Users App
"""
from django.urls import path
from . import views

urlpatterns = [
    # Authentication routes
    path('dang-nhap/', views.user_login, name='user_login'),
]
```

**📄 Code hoàn chỉnh của `users/urls.py`:**

```python
"""
URL routes for Users App
"""
from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('dang-ky/', views.RegisterView.as_view(), name='user_register'),
    path('dang-nhap/', views.user_login, name='user_login'),
    path('dang-xuat/', views.user_logout, name='user_logout'),

    # Profile (sẽ làm ở sprint khác)
    path('ho-so/', views.user_profile, name='user_profile'),
]
```

---

### 3.3 Kiểm tra `due_book/urls.py`

**Mở file:** `due_book/urls.py`

**Đảm bảo đã include users.urls:**

```python
"""
URL configuration for due_book project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),           # Routes cho books
    path('nguoi-dung/', include('users.urls')), # Routes cho users
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Lưu ý:** 
- URL login sẽ là: `http://localhost:8000/nguoi-dung/dang-nhap/`
- Named URL: `user_login`

---

### 3.4 Cấu hình `due_book/settings.py`

**Mở file:** `due_book/settings.py`

**Thêm cấu hình login ở cuối file:**

```python
# ==================== AUTHENTICATION SETTINGS ====================
# URL để redirect khi user chưa đăng nhập nhưng truy cập trang @login_required
LOGIN_URL = 'user_login'

# URL để redirect sau khi đăng nhập thành công
LOGIN_REDIRECT_URL = 'home'

# URL để redirect sau khi đăng xuất
LOGOUT_REDIRECT_URL = 'home'
```

**📄 Vị trí thêm code trong settings.py:**

```python
# ... các config khác ...

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== AUTHENTICATION SETTINGS ====================
LOGIN_URL = 'user_login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# ... rest of file ...
```

---

## 4. 🔗 Kết nối Backend với Template

### 4.1 Template đã có sẵn

File: `templates/users/user_login.html`

### 4.2 Kiểm tra Form HTML

Đảm bảo form có các thành phần sau:

```django
<form method="post">
    {% csrf_token %}

    <input type="text" name="username" class="form-control" required>
    
    <input type="password" name="password" class="form-control" required>
    
    <button type="submit">Đăng nhập</button>
</form>
```

### 4.3 Các thành phần BẮT BUỘC

| Thành phần | Giá trị | Mô tả |
|------------|---------|-------|
| `method="post"` | POST | Gửi dữ liệu bảo mật |
| `{% csrf_token %}` | - | Bảo mật chống CSRF |
| `name="username"` | username | Django AuthenticationForm yêu cầu |
| `name="password"` | password | Django AuthenticationForm yêu cầu |

### 4.4 Hiển thị lỗi trong Template

```django
{% if form.errors %}
    <div class="alert alert-danger">
        <i class="fas fa-exclamation-circle me-2"></i>
        Tên đăng nhập hoặc mật khẩu không đúng!
    </div>
{% endif %}
```

Hoặc hiển thị từng lỗi cụ thể:

```django
{% if form.errors %}
    <div class="alert alert-danger">
        <ul class="mb-0">
            {% for field in form %}
                {% for error in field.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
            {% endfor %}
            {% for error in form.non_field_errors %}
                <li>{{ error }}</li>
            {% endfor %}
        </ul>
    </div>
{% endif %}
```

### 4.5 Hiển thị Messages từ Backend

```django
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    {% endfor %}
{% endif %}
```

---

## 5. ⚠️ Xử lý lỗi đăng nhập

### 5.1 Các lỗi thường gặp

| Lỗi | Nguyên nhân | Cách xử lý |
|-----|-------------|------------|
| User không tồn tại | Username sai | Hiển thị thông báo lỗi chung |
| Sai mật khẩu | Password sai | Hiển thị thông báo lỗi chung |
| User inactive | User bị khóa | Kiểm tra `user.is_active` |
| CSRF token missing | Form thiếu csrf_token | Thêm `{% csrf_token %}` |

### 5.2 Best Practice: Thông báo lỗi chung

**Không nên** hiển thị chi tiết "Username không tồn tại" hoặc "Password sai" riêng biệt → dễ bị tấn công brute force.

**Nên** hiển thị thông báo chung: "Tên đăng nhập hoặc mật khẩu không đúng!"

```python
# Trong views.py
if form.is_valid():
    # ...
else:
    messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
```

### 5.3 Kiểm tra User Active

```python
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                # Success
            else:
                # User bị khóa
                messages.error(request, 'Tài khoản của bạn đã bị khóa!')
        else:
            # Sai username hoặc password
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
```

---

## 6. 🔄 Flow xử lý đăng nhập hoàn chỉnh

### 6.1 Flow Chart

```
┌─────────────────────────────────────────────────────────────────────┐
│                      BACKEND LOGIN FLOW                              │
└─────────────────────────────────────────────────────────────────────┘

┌─────────┐
│  USER   │
│         │
└────┬────┘
     │
     │ 1. Nhập username/password
     │ 2. Click "Đăng nhập"
     ▼
┌─────────────────┐
│  Browser gửi    │
│  POST request   │
│  /nguoi-dung/   │
│  dang-nhap/     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         DJANGO SERVER                                │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    user_login(request)                       │    │
│  │                                                              │    │
│  │  3. Nhận POST request                                        │    │
│  │           │                                                  │    │
│  │           ▼                                                  │    │
│  │  4. Tạo AuthenticationForm với POST data                     │    │
│  │           │                                                  │    │
│  │           ▼                                                  │    │
│  │  5. form.is_valid()?                                         │    │
│  │           │                                                  │    │
│  │     ┌─────┴─────┐                                            │    │
│  │     │           │                                            │    │
│  │    YES         NO                                            │    │
│  │     │           │                                            │    │
│  │     ▼           ▼                                            │    │
│  │  6. form.get_user()   9. messages.error()                    │    │
│  │     │                 'Sai tên đăng nhập                      │    │
│  │     │                  hoặc mật khẩu'                         │    │
│  │     ▼                       │                                │    │
│  │  7. login(request, user)    │                                │    │
│  │     │                       │                                │    │
│  │     ▼                       ▼                                │    │
│  │  8. messages.success()  10. Render login.html                │    │
│  │     'Chào mừng...'        với error message                  │    │
│  │     │                                                       │    │
│  │     ▼                                                       │    │
│  │  11. redirect('home')                                       │    │
│  │                                                              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│  SUCCESS:       │     │  FAILURE:       │
│  Redirect Home  │     │  Show Login     │
│  with session   │     │  with errors    │
└─────────────────┘     └─────────────────┘
```

### 6.2 Sequence Diagram

```
User         Browser         Django View        Auth Backend        Database
 │              │                  │                  │                │
 │  Submit      │                  │                  │                │
 │─────────────▶│                  │                  │                │
 │              │  POST /login     │                  │                │
 │              │  username, pwd   │                  │                │
 │              │─────────────────▶│                  │                │
 │              │                  │                  │                │
 │              │                  │  authenticate()  │                │
 │              │                  │─────────────────▶│                │
 │              │                  │                  │  Query User    │
 │              │                  │                  │───────────────▶│
 │              │                  │                  │                │
 │              │                  │                  │  User data     │
 │              │                  │                  │◀───────────────│
 │              │                  │                  │                │
 │              │                  │  User or None    │                │
 │              │                  │◀─────────────────│                │
 │              │                  │                  │                │
 │              │                  │  login()         │                │
 │              │                  │─────────────────▶│                │
 │              │                  │                  │  Create Session│
 │              │                  │                  │───────────────▶│
 │              │                  │                  │                │
 │              │  302 Redirect    │                  │                │
 │              │  Set-Cookie:     │                  │                │
 │              │  sessionid=xxx   │                  │                │
 │              │◀─────────────────│                  │                │
 │              │                  │                  │                │
 │  Redirect    │                  │                  │                │
 │  to Home     │                  │                  │                │
 │◀─────────────│                  │                  │                │
 │              │                  │                  │                │
```

### 6.3 Request/Response Flow

**Request:**
```http
POST /nguoi-dung/dang-nhap/ HTTP/1.1
Host: localhost:8000
Content-Type: application/x-www-form-urlencoded
Cookie: csrftoken=xxxxx

csrfmiddlewaretoken=xxxxx&username=testuser&password=testpass123
```

**Response (Success):**
```http
HTTP/1.1 302 Found
Location: /
Set-Cookie: sessionid=yyyyy; expires=...; HttpOnly; Path=/
```

**Response (Failure):**
```http
HTTP/1.1 200 OK
Content-Type: text/html

<!-- HTML với error message -->
```

---

## 7. ⚙️ Cấu hình settings.py chi tiết

### 7.1 Các setting quan trọng

```python
# due_book/settings.py

# URL redirect khi @login_required decorator phát hiện user chưa đăng nhập
LOGIN_URL = 'user_login'

# URL redirect sau khi đăng nhập thành công
LOGIN_REDIRECT_URL = 'home'

# URL redirect sau khi đăng xuất
LOGOUT_REDIRECT_URL = 'home'

# Thời gian session tồn tại (giây)
# Mặc định: 2 tuần
SESSION_COOKIE_AGE = 1209600

# Session expire khi đóng browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Cookie chỉ gửi qua HTTPS (production = True)
SESSION_COOKIE_SECURE = False  # True trong production
CSRF_COOKIE_SECURE = False     # True trong production
```

### 7.2 Middleware yêu cầu

Đảm bảo các middleware sau có trong `MIDDLEWARE`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ← Quản lý session
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',             # ← Bảo mật CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ← Xác thực user
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### 7.3 INSTALLED_APPS yêu cầu

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',        # ← Hệ thống authentication
    'django.contrib.contenttypes',
    'django.contrib.sessions',    # ← Quản lý session
    'django.contrib.messages',    # ← Hiển thị messages
    'django.contrib.staticfiles',
    # ...
    'users',  # App của bạn
]
```

---

## 8. 🚀 Hướng dẫn test chức năng đăng nhập

### 8.1 Tạo user để test

```bash
# Mở terminal trong thư mục project
python manage.py shell
```

```python
# Trong Python shell
from django.contrib.auth.models import User

# Tạo user mới
User.objects.create_user(username='testuser', password='testpass123')

# Kiểm tra user đã tạo
User.objects.filter(username='testuser').exists()
# Output: True
```

Hoặc dùng **createsuperuser**:

```bash
python manage.py createsuperuser
# Username: admin
# Password: admin123
```

### 8.2 Chạy server

```bash
python manage.py runserver
```

### 8.3 Test đăng nhập

1. **Mở browser:** `http://localhost:8000/nguoi-dung/dang-nhap/`

2. **Nhập thông tin:**
   - Username: `testuser`
   - Password: `testpass123`

3. **Click "Đăng nhập"**

4. **Kết quả mong đợi:**
   - Redirect đến trang chủ
   - Navbar hiển thị username thay vì "Đăng nhập"
   - Hiển thị message "Chào mừng trở lại, testuser!"

### 8.4 Test đăng nhập thất bại

1. **Nhập sai password:**
   - Username: `testuser`
   - Password: `wrongpassword`

2. **Click "Đăng nhập"**

3. **Kết quả mong đợi:**
   - Vẫn ở trang login
   - Hiển thị lỗi "Tên đăng nhập hoặc mật khẩu không đúng!"

### 8.5 Kiểm tra trong Django Admin

1. **Truy cập:** `http://localhost:8000/admin/`

2. **Đăng nhập với superuser**

3. **Vào Sessions:**
   - Click "Sessions" dưới "Authentication and Authorization"
   - Xem session đã được tạo sau khi đăng nhập

### 8.6 Debug với print statements

```python
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        # Debug: In ra dữ liệu
        print(f"POST data: {request.POST}")
        print(f"Form valid: {form.is_valid()}")
        
        if form.is_valid():
            user = form.get_user()
            print(f"User authenticated: {user.username}")
            login(request, user)
            # ...
        else:
            print(f"Form errors: {form.errors}")
            # ...
```

---

## 9. ✅ Checklist hoàn thành Sprint

### 9.1 Checklist Code

| STT | Công việc | File | Trạng thái |
|-----|-----------|------|------------|
| ☐ | Thêm function `user_login()` | `users/views.py` | ⬜ |
| ☐ | Import các module cần thiết | `users/views.py` | ⬜ |
| ☐ | Thêm route `dang-nhap/` | `users/urls.py` | ⬜ |
| ☐ | Kiểm tra include users.urls | `due_book/urls.py` | ⬜ |
| ☐ | Thêm LOGIN_URL setting | `due_book/settings.py` | ⬜ |
| ☐ | Thêm LOGIN_REDIRECT_URL setting | `due_book/settings.py` | ⬜ |

### 9.2 Checklist Template

| STT | Công việc | Trạng thái |
|-----|-----------|------------|
| ☐ | Form có `method="post"` | ⬜ |
| ☐ | Form có `{% csrf_token %}` | ⬜ |
| ☐ | Input username có `name="username"` | ⬜ |
| ☐ | Input password có `name="password"` | ⬜ |
| ☐ | Có hiển thị `form.errors` hoặc messages | ⬜ |

### 9.3 Checklist Test

| STT | Công việc | Trạng thái |
|-----|-----------|------------|
| ☐ | Tạo user test | ⬜ |
| ☐ | Đăng nhập thành công với đúng thông tin | ⬜ |
| ☐ | Đăng nhập thất bại với sai password | ⬜ |
| ☐ | Đăng nhập thất bại với user không tồn tại | ⬜ |
| ☐ | Redirect đúng sau khi đăng nhập | ⬜ |
| ☐ | Navbar hiển thị user đã đăng nhập | ⬜ |
| ☐ | Messages hiển thị đúng | ⬜ |

---

## 10. 📌 Lưu ý quan trọng

### 10.1 Sử dụng AuthenticationForm

✅ **Nên dùng** `AuthenticationForm` của Django vì:
- Đã có sẵn validation
- Tự động handle authenticate
- Có method `get_user()` để lấy user đã xác thực

```python
from django.contrib.auth.forms import AuthenticationForm

# Form này đã có sẵn:
# - validate username và password
# - method get_user()
# - error messages
```

### 10.2 Không nên tự viết authenticate logic

❌ **Không nên:**
```python
# DON'T DO THIS
user = User.objects.get(username=username)
if user.password == password:  # Password đã được hash!
    login(request, user)
```

✅ **Nên dùng:**
```python
# DO THIS
user = authenticate(request, username=username, password=password)
if user is not None:
    login(request, user)
```

### 10.3 Security Best Practices

1. **Luôn dùng HTTPS** trong production
2. **Không lưu password** trong session hay cookie
3. **Dùng CSRF token** cho mọi POST form
4. **Giới hạn số lần đăng nhập thất bại** (rate limiting)
5. **Log các hoạt động đăng nhập** để audit

### 10.4 Common Pitfalls

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|-------------|-----------|
| CSRF verification failed | Thiếu `{% csrf_token %}` | Thêm vào form |
| User không login được | Password chưa hash | Dùng `create_user()` |
| Session không lưu | Middleware thiếu | Kiểm tra MIDDLEWARE |
| Redirect không work | LOGIN_REDIRECT_URL sai | Kiểm tra named URL |

---

## 11. 📚 Tài liệu tham khảo

- [Django Authentication](https://docs.djangoproject.com/en/4.2/topics/auth/default/)
- [Django Login View](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView)
- [AuthenticationForm](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm)
- [Django Sessions](https://docs.djangoproject.com/en/4.2/topics/http/sessions/)

---

## 🎉 Tóm tắt

**Sprint này bạn cần làm:**

1. ✅ Thêm `user_login()` vào `users/views.py`
2. ✅ Thêm route vào `users/urls.py`
3. ✅ Cấu hình `settings.py`
4. ✅ Test đăng nhập

**Các file cần chỉnh sửa:**

| File | Hành động |
|------|-----------|
| `users/views.py` | Thêm function `user_login()` |
| `users/urls.py` | Thêm path `dang-nhap/` |
| `due_book/settings.py` | Thêm LOGIN_URL, LOGIN_REDIRECT_URL |

**Code chính:**

```python
# users/views.py
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Chào mừng trở lại, {user.username}!')
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
    else:
        form = AuthenticationForm()
    return render(request, 'users/user_login.html', {'form': form})
```

**Sprint sau sẽ làm:**
- Logout functionality
- Change password
- Profile management

---

*Document created for Sprint Backend Login - DUE Book Project*