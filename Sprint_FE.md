# Sprint Front-end: Chức năng Đăng nhập (Login)

## 📋 Thông tin Sprint

| Thông tin | Chi tiết |
|-----------|----------|
| **Sprint Name** | Front-end Login |
| **Mục tiêu** | Hoàn thành giao diện đăng nhập |
| **Thời gian** | 1-2 ngày |
| **Backend** | Chưa triển khai (Sprint sau) |

---

## ⚡ HƯỚNG DẪN NHANH (3 BƯỚC)

### 📂 Bước 1: Mở thư mục `templates/users/`

```
📁 Project B (Book_DUE)
 └── 📁 templates/
      └── 📁 users/          ← Mở thư mục này
```

### 📄 Bước 2: Tạo file mới `user_login.html`

- **Right-click** vào thư mục `users` → **New File**
- Gõ tên: `user_login.html`
- Nhấn **Enter**

### 📋 Bước 3: Copy code và Paste

Copy toàn bộ code từ **Section 6** bên dưới vào file vừa tạo, sau đó nhấn **Ctrl + S** để lưu.

---

## ✅ KẾT QUẢ SAU KHI HOÀN THÀNH

```
📁 templates/
 └── 📁 users/
     ├── user_register.html   ← Đã có
     └── user_login.html      ← ✅ FILE MỚI TẠO
```

---

## 1. 🎯 Sprint Goal

Hoàn thành **giao diện người dùng (Front-end)** cho chức năng **Đăng nhập**:

- ✅ Giao diện form login đẹp, responsive
- ✅ Tương thích với `base.html` đã có
- ✅ Sử dụng Bootstrap 5 (đã có sẵn trong base.html)
- ✅ Chuẩn bị form HTML để kết nối Backend ở Sprint sau
- ✅ Có link chuyển sang trang Register

---

## 2. 📊 Phân tích các thành phần Front-end của trang Login

### 2.1 Cấu trúc Form Login

```
┌─────────────────────────────────────────┐
│              ĐĂNG NHẬP                  │
├─────────────────────────────────────────┤
│  ┌─────────────────────────────────┐    │
│  │ Tên đăng nhập                   │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ Mật khẩu                        │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │        🔐 ĐĂNG NHẬP             │    │
│  └─────────────────────────────────┘    │
│                                         │
│  Chưa có tài khoản? [Đăng ký]           │
└─────────────────────────────────────────┘
```

### 2.2 Các thành phần chính

| Thành phần | Loại | Mô tả |
|------------|------|-------|
| **Input Username** | `<input type="text">` | Nhập tên đăng nhập |
| **Input Password** | `<input type="password">` | Nhập mật khẩu (hidden) |
| **Button Login** | `<button type="submit">` | Nút gửi form |
| **Link Register** | `<a href="...">` | Link sang trang đăng ký |
| **Error Display** | `<div class="alert">` | Hiển thị lỗi (nếu có) |

### 2.3 Thư viện đã có sẵn trong base.html

✅ **Bootstrap 5.3.0** - CSS Framework
✅ **Font Awesome 6.4.0** - Icons
✅ **Google Fonts (Inter)** - Typography
✅ **Custom CSS (base.css)** - Style tùy chỉnh

---

## 3. 📂 Hướng dẫn copy file từ Project A sang Project B

### 3.1 File cần copy

| File nguồn (Project A) | File đích (Project B) | Mô tả |
|------------------------|----------------------|-------|
| `templates/users/user_login.html` | `templates/users/user_login.html` | Template trang login |

### 3.2 Các file đã có sẵn trong Project B (không cần copy)

| File | Mô tả |
|------|-------|
| `templates/base.html` | Template gốc đã có |
| `static/css/base.css` | CSS chung đã có |
| `static/js/main.js` | JavaScript chung |

### 3.3 Thư viện CDN (tự động load từ base.html)

```html
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

---

## 4. 📁 Hướng dẫn đặt file vào đúng thư mục trong Project B

### 4.1 Cấu trúc thư mục Project B sau khi hoàn thành

```
due_book/
│
├── books/
├── ratings/
├── static/
│   ├── css/
│   │   └── base.css          ← Đã có sẵn
│   ├── images/
│   └── js/
│       └── main.js           ← Đã có sẵn
│
├── templates/
│   ├── base.html             ← Đã có sẵn
│   └── users/
│       ├── user_register.html ← Đã có sẵn
│       └── user_login.html    ← 📝 FILE MỚI CẦN TẠO
│
├── due_book/
│   ├── settings.py
│   └── urls.py
│
├── users/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
└── manage.py
```

---

## 4.2 🖥️ Hướng dẫn chi tiết TỪNG BƯỚC tạo file (VS Code)

### 📌 Bước 1: Mở Project B trong VS Code

1. **Mở VS Code**
2. **File → Open Folder** (hoặc `Ctrl + K, Ctrl + O`)
3. **Chọn thư mục Project B** của bạn
4. **Nhấn "Select Folder"**

```
Ví dụ đường dẫn Project B:
D:\2_HOC_KI\6_SEMESTER\3.Quan_Tri_Du_An\BACK_UP\Book_DUE
```

---

### 📌 Bước 2: Mở thư mục `templates/users/`

Trong **Explorer** (panel bên trái), điều hướng theo đường dẫn:

```
📁 templates/
   └── 📁 users/
       ├── 📄 user_register.html  ← File đã có
       └── 📄 user_login.html     ← Cần tạo file này
```

**Cách mở:**
1. Click vào **▶ templates** để mở rộng
2. Click vào **▶ users** để mở rộng
3. Bạn sẽ thấy file `user_register.html` đã có sẵn

---

### 📌 Bước 3: Tạo file mới `user_login.html`

**Cách 1: Click chuột phải**
1. **Right-click** vào thư mục `users`
2. Chọn **"New File"**
3. Gõ tên: `user_login.html`
4. Nhấn **Enter**

**Cách 2: Phím tắt**
1. Click vào thư mục `users` để chọn
2. Nhấn phím **Ctrl + N** (tạo file mới)
3. Gõ tên: `user_login.html`
4. Nhấn **Enter**

**Cách 3: Tạo file trống rồi Save**
1. Nhấn **Ctrl + N** (tạo file trống)
2. Copy code từ **Section 6** bên dưới
3. Paste vào file
4. Nhấn **Ctrl + S** để Save
5. Chọn lưu vào: `templates/users/user_login.html`

---

### 📌 Bước 4: Copy và Paste code

**4.1. Copy code từ Section 6 bên dưới** (hoặc từ Project A)

**4.2. Paste vào file `user_login.html` vừa tạo**

**4.3. Nhấn `Ctrl + S` để lưu file**

---

### 📌 Bước 5: Kiểm tra file đã tạo đúng chưa

Trong **Explorer**, cấu trúc thư mục `templates/users/` sẽ như sau:

```
📁 templates/
   └── 📁 users/
       ├── 📄 user_change_password.html
       ├── 📄 user_edit_profile.html
       ├── 📄 user_login.html           ← ✅ FILE MỚI TẠO
       ├── 📄 user_profile.html
       └── 📄 user_register.html
```

---

### 📌 Bước 6: Kiểm tra nội dung file

Mở file `user_login.html` và đảm bảo có các dòng sau:

```django
{% extends 'base.html' %}        ← Dòng 1: Kế thừa base.html

{% block title %}...{% endblock %}  ← Định nghĩa title

{% block content %}              ← Nội dung chính
    ...
    <form method="post">         ← Form POST
        {% csrf_token %}         ← CSRF token (BẮT BUỘC)
        ...
        <input name="username">  ← Input username
        <input name="password">  ← Input password
        ...
    </form>
    ...
{% endblock %}
```

---

## 4.3 📋 Tóm tắt nhanh - Chỉ 3 bước đơn giản

| Bước | Hành động | Chi tiết |
|------|-----------|----------|
| **1** | Mở thư mục `templates/users/` | Trong VS Code Explorer |
| **2** | Tạo file `user_login.html` | Right-click → New File |
| **3** | Copy code từ Section 6 | Paste và Save (Ctrl+S) |

**Đường dẫn đầy đủ của file mới:**
```
templates/users/user_login.html
```

---

## 5. 🔧 Hướng dẫn chỉnh sửa template

### 5.1 Các nguyên tắc quan trọng

1. **Kế thừa từ base.html**
```django
{% extends 'base.html' %}
```

2. **Load static files** (nếu dùng CSS/JS riêng)
```django
{% load static %}
```

3. **Định nghĩa title trang**
```django
{% block title %}Đăng nhập - DUE Book{% endblock %}
```

4. **Nội dung chính trong block content**
```django
{% block content %}
    <!-- Form login ở đây -->
{% endblock %}
```

### 5.2 Các class Bootstrap quan trọng

| Class | Mục đích |
|-------|----------|
| `container` | Container chính |
| `row justify-content-center` | Căn giữa hàng |
| `col-md-5` | Cột width 5/12 |
| `card` | Card container |
| `card-header bg-primary text-white` | Header card màu primary |
| `card-body` | Body card |
| `card-footer` | Footer card |
| `form-control` | Input styling |
| `form-label` | Label styling |
| `btn btn-primary btn-lg` | Button primary lớn |
| `d-grid` | Display grid (full width button) |
| `alert alert-danger` | Alert lỗi |

---

## 6. 💻 Code hoàn chỉnh: templates/users/user_login.html

```django
{% extends 'base.html' %}

{% block title %}Đăng nhập - DUE Book{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-md-5">
            <div class="card">
                <div class="card-header bg-primary text-white text-center">
                    <h4 class="mb-0"><i class="fas fa-sign-in-alt me-2"></i>Đăng nhập</h4>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}

                        <div class="mb-3">
                            <label class="form-label">Tên đăng nhập</label>
                            <input type="text" name="username" class="form-control" required autofocus>
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Mật khẩu</label>
                            <input type="password" name="password" class="form-control" required>
                        </div>

                        {% if form.errors %}
                            <div class="alert alert-danger">
                                {{ form.errors }}
                            </div>
                        {% endif %}

                        <div class="d-grid">
                            <button type="submit" class="btn btn-primary btn-lg">
                                <i class="fas fa-sign-in-alt me-1"></i>Đăng nhập
                            </button>
                        </div>
                    </form>
                </div>
                <div class="card-footer text-center">
                    <small class="text-muted">
                        Chưa có tài khoản? <a href="{% url 'user_register' %}">Đăng ký</a>
                    </small>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 7. 📝 Chuẩn bị form HTML để kết nối Backend

### 7.1 Các thành phần bắt buộc cho Backend

| Thành phần | Giá trị | Mục đích |
|------------|---------|----------|
| `method="post"` | POST | Gửi dữ liệu bảo mật |
| `{% csrf_token %}` | CSRF Token | Bảo mật form Django |
| `name="username"` | username | Backend nhận diện field |
| `name="password"` | password | Backend nhận diện field |
| `type="password"` | password | Ẩn ký tự mật khẩu |
| `required` | - | Validate client-side |

### 7.2 Giải thích các thuộc tính quan trọng

```html
<!-- Form sử dụng method POST để bảo mật dữ liệu -->
<form method="post">
    
    <!-- CSRF Token - BẮT BUỘC trong Django để chống tấn công CSRF -->
    {% csrf_token %}

    <!-- Input Username -->
    <input type="text" 
           name="username"     <!-- name phải là "username" để Django AuthenticationForm nhận diện -->
           class="form-control" 
           required            <!-- Validate bắt buộc nhập -->
           autofocus>          <!-- Tự động focus khi load trang -->

    <!-- Input Password -->
    <input type="password"     <!-- type="password" để ẩn ký tự -->
           name="password"     <!-- name phải là "password" để Django AuthenticationForm nhận diện -->
           class="form-control" 
           required>

    <!-- Submit Button -->
    <button type="submit">Đăng nhập</button>
</form>
```

### 7.3 Hiển thị lỗi từ Backend

```django
{% if form.errors %}
    <div class="alert alert-danger">
        <!-- Hiển thị lỗi khi Backend validate thất bại -->
        {% for field in form %}
            {% for error in field.errors %}
                {{ error }}
            {% endfor %}
        {% endfor %}
        {% for error in form.non_field_errors %}
            {{ error }}
        {% endfor %}
    </div>
{% endif %}
```

Hoặc đơn giản hơn:

```django
{% if form.errors %}
    <div class="alert alert-danger">
        <i class="fas fa-exclamation-circle me-2"></i>
        Tên đăng nhập hoặc mật khẩu không đúng!
    </div>
{% endif %}
```

---

## 8. 🔄 Flow hoạt động của Front-end Login

### 8.1 Flow Chart

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONT-END LOGIN FLOW                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────┐     ┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  USER   │────▶│  Nhập       │────▶│  Click       │────▶│  Gửi POST   │
│         │     │  Username   │     │  "Đăng nhập" │     │  Request    │
│         │     │  Password   │     │              │     │  to Server  │
└─────────┘     └─────────────┘     └──────────────┘     └──────┬──────┘
                                                                  │
                                                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                     ┌───┐
│                         BACKEND (Sprint sau)                        │   │
│                                                                     │ │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────┐   │ │
│  │  Receive    │────▶│  Validate    │────▶│  Authenticate       │   │ │
│  │  POST Data  │     │  Form        │     │  User               │   │ │
│  └─────────────┘     └──────────────┘     └──────────┬──────────┘   │ │
│                                                      │              │ │
│                                         ┌────────────┴───────────┐  │ │
│                                         ▼                        ▼  │ │
│                                  ┌──────────┐            ┌──────────┐│ │
│                                  │ SUCCESS  │            │  ERROR   ││ │
│                                  │ Login    │            │  Show    ││ │
│                                  │ OK       │            │  form    ││ │
│                                  └────┬─────┘            └────┬─────┘│ │
│                                       │                       │      │ │
└───────────────────────────────────────┼───────────────────────┼──────┘ │
                                        │                       │        │
                                        ▼                       ▼        │
                                 ┌─────────────┐         ┌─────────────┐ │
                                 │  Redirect   │         │  Render     │ │
                                 │  to Home    │         │  Login      │ │
                                 │  Page       │         │  with Error │ │
                                 └─────────────┘         └─────────────┘ │
                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Sequence Diagram

```
User                Browser              Django Server
 │                     │                       │
 │  1. Truy cập /login │                       │
 │────────────────────▶│                       │
 │                     │  2. GET /login        │
 │                     │──────────────────────▶│
 │                     │                       │
 │                     │  3. Return HTML       │
 │                     │◀──────────────────────│
 │                     │                       │
 │  4. Hiển thị form   │                       │
 │◀────────────────────│                       │
 │                     │                       │
 │  5. Nhập username,  │                       │
 │     password        │                       │
 │────────────────────▶│                       │
 │                     │                       │
 │  6. Click Login     │                       │
 │────────────────────▶│                       │
 │                     │  7. POST /login       │
 │                     │  (csrf_token, data)   │
 │                     │──────────────────────▶│
 │                     │                       │
 │                     │     [Sprint sau]     │
 │                     │                       │
```

### 8.3 Request/Response Structure

**Request (khi submit form):**
```http
POST /users/login/ HTTP/1.1
Host: localhost:8000
Content-Type: application/x-www-form-urlencoded
Cookie: csrftoken=xxxxx

csrfmiddlewaretoken=xxxxx&username=myuser&password=mypassword
```

**Response Success (Sprint sau):**
```http
HTTP/1.1 302 Found
Location: /
Set-Cookie: sessionid=xxxxx
```

**Response Error (Sprint sau):**
```http
HTTP/1.1 200 OK
Content-Type: text/html

<!-- HTML với error message -->
```

---

## 9. ✅ Checklist hoàn thành Sprint

### 9.1 Checklist tạo file

| STT | Công việc | Trạng thái |
|-----|-----------|------------|
| ☐ | Tạo file `templates/users/user_login.html` | ⬜ |
| ☐ | Copy nội dung template từ Section 6 | ⬜ |
| ☐ | Kiểm tra template extends `base.html` đúng | ⬜ |
| ☐ | Kiểm tra có `{% csrf_token %}` trong form | ⬜ |

### 9.2 Checklist cấu trúc form

| STT | Công việc | Trạng thái |
|-----|-----------|------------|
| ☐ | Input username có `name="username"` | ⬜ |
| ☐ | Input password có `name="password"` | ⬜ |
| ☐ | Input password có `type="password"` | ⬜ |
| ☐ | Form có `method="post"` | ⬜ |
| ☐ | Button có `type="submit"` | ⬜ |

### 9.3 Checklist giao diện

| STT | Công việc | Trạng thái |
|-----|-----------|------------|
| ☐ | Form hiển thị đẹp, căn giữa màn hình | ⬜ |
| ☐ | Card header có icon + text "Đăng nhập" | ⬜ |
| ☐ | Button login có icon 🔐 | ⬜ |
| ☐ | Có link "Đăng ký" ở footer card | ⬜ |
| ☐ | Responsive trên mobile | ⬜ |

### 9.4 Checklist tích hợp

| STT | Công việc | Trạng thái |
|-----|-----------|------------|
| ☐ | Link register trỏ đến `{% url 'user_register' %}` | ⬜ |
| ☐ | Navbar hiển thị link "Đăng nhập" (từ base.html) | ⬜ |
| ☐ | CSS Bootstrap load đúng từ base.html | ⬜ |
| ☐ | Font Awesome icons hiển thị đúng | ⬜ |

---

## 10. 🚀 Hướng dẫn test Front-end

### 10.1 Test hiển thị trang Login

Sau khi Backend hoàn thành (Sprint sau), bạn có thể test:

```bash
# Chạy server
python manage.py runserver

# Truy cập
http://localhost:8000/users/login/
```

### 10.2 Test tạm thời (chưa cần Backend)

Tạo một URL tạm trong `users/urls.py` để test:

```python
# users/urls.py
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # URL tạm để test front-end
    path('login/', TemplateView.as_view(template_name='users/user_login.html'), name='user_login'),
]
```

### 10.3 Kiểm tra Elements trong Browser

1. Mở Chrome DevTools (F12)
2. Kiểm tra tab **Elements**:
   - Form có `method="post"` không?
   - CSRF token có được render không?
   - Input có `name` đúng không?

3. Kiểm tra tab **Network**:
   - Submit form và xem request được gửi

---

## 11. 📌 Lưu ý quan trọng

### 11.1 Không cần copy

❌ **Không cần copy CSS riêng** - Trang login sử dụng CSS từ `base.css` và Bootstrap

❌ **Không cần copy JS riêng** - Trang login không cần JavaScript đặc biệt

❌ **Không cần copy views.py, forms.py** - Đây là Backend, sẽ làm ở Sprint sau

### 11.2 Tương thích với Register

Trang Login nên có style tương đồng với trang Register:

| Trang | Header | Footer |
|-------|--------|--------|
| Login | "Đăng nhập" | Link "Đăng ký" |
| Register | "Đăng ký tài khoản" | Link "Đăng nhập" |

### 11.3 Chuẩn bị cho Backend Sprint

Front-end đã chuẩn bị sẵn:

✅ Form với `method="POST"`
✅ CSRF token
✅ Input `name="username"` và `name="password"`
✅ Hiển thị error từ form.errors

Backend Sprint chỉ cần:
- Tạo `AuthenticationForm` 
- Viết view `user_login`
- Cấu hình URL

---

## 12. 📚 Tài liệu tham khảo

- [Django Authentication Views](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView)
- [Bootstrap 5 Forms](https://getbootstrap.com/docs/5.3/forms/overview/)
- [Django CSRF Protection](https://docs.djangoproject.com/en/4.2/ref/csrf/)

---

## 🎉 Tóm tắt

**Sprint này bạn cần làm:**

1. ✅ Tạo file `templates/users/user_login.html`
2. ✅ Copy code từ Section 6 vào file
3. ✅ Kiểm tra form có đúng cấu trúc không
4. ✅ Test hiển thị trên browser

**File duy nhất cần tạo:**
```
templates/users/user_login.html
```

**Sprint sau sẽ làm:**
- Views xử lý login
- Forms validation
- Authentication
- Session management

---

*Document created for Sprint Front-end Login - DUE Book Project*