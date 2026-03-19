# HƯỚNG DẪN QUẢN LÝ DỰ ÁN DUE BOOK

> **Tài liệu hướng dẫn Scrum/Agile cho nhóm phát triển**
> 
> Ngày tạo: 22/02/2026 | Phiên bản: 1.0

---

## MỤC LỤC

1. [Tổng quan dự án](#1-tổng-quan-dự-án)
2. [Danh sách Module](#2-danh-sách-module)
3. [User Stories & Dependency Map](#3-user-stories--dependency-map)
4. [Sprint Planning đề xuất](#4-sprint-planning-đề-xuất)
5. [Phân rã Task chi tiết](#5-phân-rã-task-chi-tiết)
6. [Hướng dẫn tạo Sprint trong Jira](#6-hướng-dẫn-tạo-sprint-trong-jira)
7. [Cách theo dõi Burndown chart](#7-cách-theo-dõi-burndown-chart)
8. [Checklist trước khi Review Sprint](#8-checklist-trước-khi-review-sprint)

---

## 1. TỔNG QUAN DỰ ÁN

### 1.1 Mục tiêu chính của hệ thống

**DUE Book** là nền tảng mua bán/trao đổi sách cũ dành riêng cho sinh viên Đại học Kinh tế (DUE). Hệ thống giúp:

| Mục tiêu | Mô tả |
|----------|-------|
| 🎯 **Kết nối** | Kết nối người bán và người mua sách cũ trong trường |
| 💰 **Tiết kiệm** | Giúp sinh viên tiết kiệm chi phí mua sách (giảm đến 80%) |
| 🔄 **Tái sử dụng** | Tối ưu hóa vòng đời sách, giảm lãng phí |
| ⭐ **Uy tín** | Hệ thống đánh giá giúp xây dựng niềm tin giữa người dùng |
| 📱 **Tiện lợi** | Giao diện thân thiện, dễ sử dụng trên mọi thiết bị |

### 1.2 Công nghệ sử dụng

| Thành phần | Công nghệ |
|------------|-----------|
| **Backend** | Django 5.x (Python) |
| **Frontend** | Bootstrap 5, HTML5, CSS3, JavaScript |
| **Database** | SQLite (phát triển) / PostgreSQL (production) |
| **Authentication** | Django Auth System |
| **File Storage** | Django Media Storage |
| **Testing** | Django TestCase |

### 1.3 Cấu trúc dự án

```
1.Code_Project/
├── due_book/              # Cấu hình Django settings
├── books/                 # Module quản lý sách
│   ├── models.py         # Book, Subject, PurchaseRequest
│   ├── views.py          # CRUD sách, purchase flow
│   ├── forms.py          # BookForm, BookSearchForm
│   └── urls.py           # Routing
├── users/                 # Module quản lý người dùng
│   ├── models.py         # UserProfile
│   ├── views.py          # Auth, Profile
│   └── forms.py          # Register, Profile forms
├── ratings/               # Module đánh giá
│   ├── models.py         # Rating
│   ├── views.py          # CRUD đánh giá
│   └── forms.py          # RatingForm
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
└── media/                 # User uploaded files
```

---

## 2. DANH SÁCH MODULE

### 2.1 Module Users (Quản lý người dùng)

| Chức năng | Mô tả | Status |
|-----------|-------|--------|
| Đăng ký | Tạo tài khoản mới với thông tin liên hệ | ✅ Hoàn thành |
| Đăng nhập | Xác thực người dùng | ✅ Hoàn thành |
| Đăng xuất | Kết thúc phiên làm việc | ✅ Hoàn thành |
| Hồ sơ cá nhân | Xem/chỉnh sửa thông tin cá nhân | ✅ Hoàn thành |
| Đổi mật khẩu | Thay đổi mật khẩu | ✅ Hoàn thành |

**Models:**
- `User` (Django built-in)
- `UserProfile` - Mở rộng thông tin user (phone, facebook, zalo, avatar, bio)

### 2.2 Module Books (Quản lý sách)

| Chức năng | Mô tả | Status |
|-----------|-------|--------|
| Đăng bán sách | Tạo bài đăng bán sách mới | ✅ Hoàn thành |
| Danh sách sách | Xem tất cả sách đang bán | ✅ Hoàn thành |
| Chi tiết sách | Xem thông tin chi tiết | ✅ Hoàn thành |
| Tìm kiếm | Tìm theo tên, tác giả, mô tả | ✅ Hoàn thành |
| Lọc | Lọc theo môn học, tình trạng, giá | ✅ Hoàn thành |
| Sắp xếp | Sắp xếp theo giá, ngày đăng | ✅ Hoàn thành |
| Sửa/Xóa | Chỉnh sửa hoặc xóa bài đăng | ✅ Hoàn thành |
| Sách của tôi | Quản lý sách đã đăng | ✅ Hoàn thành |

**Models:**
- `Subject` - Danh mục môn học
- `Book` - Thông tin sách (title, price, condition, status, seller, buyer...)
- `BookImage` - Ảnh phụ của sách
- `PurchaseRequest` - Yêu cầu mua sách

### 2.3 Module Purchase Request (Yêu cầu mua)

| Chức năng | Mô tả | Status |
|-----------|-------|--------|
| Gửi yêu cầu | Người mua gửi yêu cầu mua sách | ✅ Hoàn thành |
| Duyệt yêu cầu | Người bán xác nhận giao dịch | ✅ Hoàn thành |
| Từ chối | Người bán từ chối yêu cầu | ✅ Hoàn thành |
| Sách đã mua | Xem sách đã mua thành công | ✅ Hoàn thành |

**Status Flow:**
```
PENDING → APPROVED (Sách bán thành công)
        → REJECTED (Yêu cầu bị từ chối)
```

### 2.4 Module Ratings (Đánh giá)

| Chức năng | Mô tả | Status |
|-----------|-------|--------|
| Đánh giá người bán | Đánh giá sau khi mua hàng | ✅ Hoàn thành |
| Xem đánh giá | Xem tất cả đánh giá của user | ✅ Hoàn thành |
| Tính điểm uy tín | Tự động cập nhật reputation | ✅ Hoàn thành |

**Models:**
- `Rating` - Đánh giá (seller, reviewer, book, rating 1-5, comment)

---

## 3. USER STORIES & DEPENDENCY MAP

### 3.1 Danh sách User Stories

| ID | User Story | Priority | Story Points | Status |
|----|------------|----------|--------------|--------|
| **US01** | Đăng ký tài khoản mới | High | 5 | ✅ Hoàn thành |
| **US02** | Đăng nhập vào hệ thống | High | 3 | ✅ Hoàn thành |
| **US03** | Quản lý hồ sơ cá nhân | Medium | 5 | ✅ Hoàn thành |
| **US04** | Đăng bán sách | High | 8 | ✅ Hoàn thành |
| **US05** | Xem danh sách sách | High | 5 | ✅ Hoàn thành |
| **US06** | Tìm kiếm và lọc sách | High | 5 | ✅ Hoàn thành |
| **US07** | Xem chi tiết sách | High | 3 | ✅ Hoàn thành |
| **US08** | Chỉnh sửa/Xóa bài đăng | Medium | 3 | ✅ Hoàn thành |
| **US09** | Gửi yêu cầu mua sách | High | 5 | ✅ Hoàn thành |
| **US10** | Duyệt/Từ chối yêu cầu mua | High | 5 | ✅ Hoàn thành |
| **US11** | Xem sách đã mua | Medium | 3 | ✅ Hoàn thành |
| **US12** | Đánh giá người bán | Medium | 5 | ✅ Hoàn thành |
| **US13** | Xem đánh giá người bán | Low | 3 | ✅ Hoàn thành |
| **US14** | Xem thông tin liên hệ | Medium | 2 | ✅ Hoàn thành |

### 3.2 Chi tiết User Stories

#### US01 - Đăng ký tài khoản mới
```
AS A Sinh viên mới
I WANT TO Đăng ký tài khoản với thông tin liên hệ
SO THAT Có thể tham gia mua bán trên hệ thống

ACCEPTANCE CRITERIA:
- Form đăng ký gồm: username, email, password, họ tên
- Bắt buộc nhập số điện thoại, link Facebook, link Zalo
- Validate trùng username
- Validate mật khẩu xác nhận
- Tự động tạo UserProfile sau khi đăng ký
```

#### US02 - Đăng nhập vào hệ thống
```
AS A Người dùng đã có tài khoản
I WANT TO Đăng nhập với username/password
SO THAT Truy cập các chức năng của hệ thống

ACCEPTANCE CRITERIA:
- Form đăng nhập với username, password
- Hiển thị thông báo lỗi khi sai thông tin
- Redirect đến trang yêu cầu sau khi login
- Lưu session đăng nhập
```

#### US03 - Quản lý hồ sơ cá nhân
```
AS A Người dùng đã đăng nhập
I WANT TO Xem và chỉnh sửa thông tin cá nhân
SO THAT Cập nhật thông tin liên hệ, avatar

ACCEPTANCE CRITERIA:
- Xem được hồ sơ của mình và người khác
- Chỉnh sửa được: avatar, bio, phone, facebook, zalo
- Đổi được mật khẩu
- Hiển thị thống kê: số sách đã bán, điểm uy tín
```

#### US04 - Đăng bán sách
```
AS A Sinh viên có sách cũ
I WANT TO Đăng bài bán sách với đầy đủ thông tin
SO THAT Người khác có thể tìm và mua sách

ACCEPTANCE CRITERIA:
- Form gồm: tên sách, tác giả, môn học, giá bán, giá bìa
- Chọn tình trạng sách (Mới, Like new, Khá, Trung bình, Cũ)
- Upload ảnh bìa
- Tự động hiển thị thông tin liên hệ từ UserProfile
- Validate giá tối thiểu 1,000 VNĐ
```

#### US05 - Xem danh sách sách
```
AS A Người mua
I WANT TO Xem danh sách tất cả sách đang bán
SO THAT Tìm sách phù hợp với nhu cầu

ACCEPTANCE CRITERIA:
- Hiển thị dạng grid/list với phân trang (20 sách/trang)
- Mỗi sách hiển thị: ảnh, tên, giá, tình trạng, người bán
- Chỉ hiển thị sách có status='available'
- Loading nhanh với select_related/prefetch_related
```

#### US06 - Tìm kiếm và lọc sách
```
AS A Người mua
I WANT TO Tìm kiếm sách theo tiêu chí
SO THAT Nhanh chóng tìm được sách mong muốn

ACCEPTANCE CRITERIA:
- Tìm theo tên sách, tác giả, mô tả (LIKE query)
- Lọc theo: Môn học, Tình trạng sách, Khoảng giá
- Sắp xếp theo: Mới nhất, Giá, Lượt xem
- Giữ nguyên filter khi chuyển trang
```

#### US07 - Xem chi tiết sách
```
AS A Người mua
I WANT TO Xem thông tin chi tiết của sách
SO THAT Quyết định có mua hay không

ACCEPTANCE CRITERIA:
- Hiển thị đầy đủ thông tin sách
- Hiển thị % giảm giá nếu có giá bìa
- Hiển thị thông tin liên hệ người bán
- Hiển thị sách tương tự, sách cùng người bán
- Tăng lượt xem khi xem chi tiết
```

#### US08 - Chỉnh sửa/Xóa bài đăng
```
AS A Người bán
I WANT TO Chỉnh sửa hoặc xóa bài đăng
SO THAT Cập nhật thông tin hoặc hủy bán

ACCEPTANCE CRITERIA:
- Chỉ chủ sở hữu mới được sửa/xóa
- Form chỉnh sửa giống form đăng
- Xác nhận trước khi xóa
- Đánh dấu đã bán (không xóa)
```

#### US09 - Gửi yêu cầu mua sách
```
AS A Người mua
I WANT TO Gửi yêu cầu mua sách
SO THAT Người bán biết tôi muốn mua

ACCEPTANCE CRITERIA:
- Nút "Tôi đã mua sách này" trên trang chi tiết
- Không thể mua sách của chính mình
- Không thể mua sách đã bán
- Mỗi user chỉ gửi 1 yêu cầu cho 1 sách
- Status mặc định là PENDING
```

#### US10 - Duyệt/Từ chối yêu cầu mua
```
AS A Người bán
I WANT TO Duyệt hoặc từ chối yêu cầu mua
SO THAT Xác nhận giao dịch với người mua phù hợp

ACCEPTANCE CRITERIA:
- Xem danh sách yêu cầu đang chờ
- Duyệt → Book.status = 'sold', Book.buyer = buyer
- Từ chối → Request.status = 'rejected'
- Khi duyệt 1 request, các request khác tự động rejected
```

#### US11 - Xem sách đã mua
```
AS A Người mua
I WANT TO Xem danh sách sách đã mua
SO THAT Theo dõi lịch sử giao dịch

ACCEPTANCE CRITERIA:
- Chỉ hiển thị sách có buyer = current_user
- Hiển thị trạng thái đánh giá
- Link đến trang đánh giá
```

#### US12 - Đánh giá người bán
```
AS A Người mua đã giao dịch
I WANT TO Đánh giá người bán
SO THAT Giúp người khác biết uy tín của seller

ACCEPTANCE CRITERIA:
- Chỉ buyer đã được APPROVED mới được đánh giá
- Đánh giá 1-5 sao + bình luận
- Không thể tự đánh giá mình
- Không thể đánh giá 2 lần cho cùng 1 sách
- Tự động cập nhật điểm uy tín seller
```

#### US13 - Xem đánh giá người bán
```
AS A Người mua
I WANT TO Xem đánh giá của người bán
SO THAT Đánh giá độ uy tín trước khi mua

ACCEPTANCE CRITERIA:
- Hiển thị trên profile người bán
- Thống kê: điểm trung bình, số lượt đánh giá
- Phân bố đánh giá theo sao
```

#### US14 - Xem thông tin liên hệ
```
AS A Người mua
I WANT TO Xem thông tin liên hệ người bán
SO THAT Liên hệ để giao dịch

ACCEPTANCE CRITERIA:
- Hiển thị phone, facebook, zalo từ UserProfile
- Hiển thị trên trang chi tiết sách
- Link trực tiếp đến Facebook/Zalo
```

### 3.3 Dependency Map (Quan hệ phụ thuộc)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEPENDENCY GRAPH                                  │
└─────────────────────────────────────────────────────────────────────┘

                    ┌──────────────┐
                    │  US01 Đăng ký │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │ US02 Đăng nhập│
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
    │ US03 Profile│ │ US04 Đăng   │ │ US05 Xem    │
    │             │ │ bán sách    │ │ danh sách   │
    └─────────────┘ └──────┬──────┘ └──────┬──────┘
                           │               │
                    ┌──────▼──────┐ ┌──────▼──────┐
                    │ US08 Sửa/   │ │ US06 Tìm    │
                    │ Xóa bài     │ │ kiếm sách   │
                    └─────────────┘ └──────┬──────┘
                                          │
                                   ┌──────▼──────┐
                                   │ US07 Chi    │
                                   │ tiết sách   │
                                   └──────┬──────┘
                                          │
                           ┌──────────────┼──────────────┐
                           │              │              │
                    ┌──────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
                    │ US09 Gửi    │ │ US14 Thông │ │ US11 Sách  │
                    │ yêu cầu     │ │ tin liên hệ│ │ đã mua     │
                    └──────┬──────┘ └────────────┘ └─────┬──────┘
                           │                              │
                    ┌──────▼──────┐                       │
                    │ US10 Duyệt  │                       │
                    │ yêu cầu     │                       │
                    └──────┬──────┘                       │
                           │                              │
                    ┌──────▼──────┐                       │
                    │ US12 Đánh   │◄──────────────────────┘
                    │ giá         │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ US13 Xem    │
                    │ đánh giá    │
                    └─────────────┘
```

### 3.4 Bảng Dependency chi tiết

| US | Phụ thuộc vào | Lý do |
|----|---------------|-------|
| US02 | US01 | Phải có tài khoản mới đăng nhập được |
| US03 | US02 | Phải đăng nhập mới quản lý profile |
| US04 | US02 | Phải đăng nhập mới đăng bán sách |
| US05 | - | Không cần đăng nhập để xem |
| US06 | US05 | Tìm kiếm dựa trên danh sách sách |
| US07 | US05 | Chi tiết là trang con của danh sách |
| US08 | US04 | Phải có bài đăng mới sửa/xóa được |
| US09 | US02, US07 | Phải đăng nhập và xem sách để mua |
| US10 | US09 | Phải có yêu cầu mới duyệt được |
| US11 | US10 | Phải được duyệt mới có sách đã mua |
| US12 | US10, US11 | Phải giao dịch thành công mới đánh giá |
| US13 | US12 | Phải có đánh giá mới xem được |
| US14 | US07 | Thông tin hiển thị trên trang chi tiết |

---

## 4. SPRINT PLANNING ĐỀ XUẤT

### 4.1 Phân bổ Sprint (5 Sprint - 2 tuần/Sprint)

#### 📌 SPRINT 1 - Nền tảng & Authentication (Tuần 1-2)

**🎯 Sprint Goal:** Thiết lập nền tảng dự án và hệ thống authentication

| US ID | User Story | Story Points |
|-------|------------|--------------|
| US01 | Đăng ký tài khoản | 5 |
| US02 | Đăng nhập/Đăng xuất | 3 |
| US03 | Quản lý hồ sơ cá nhân | 5 |
| **Total** | | **13 SP** |

**📋 Lý do sắp xếp:**
- Đây là các tính năng nền tảng, mọi tính năng khác đều phụ thuộc
- Đăng ký/Đăng nhập phải hoạt động trước khi làm bất cứ điều gì
- Profile cần thiết để lưu thông tin liên hệ

**⚠️ Rủi ro:**
- Thiết lập môi trường development có thể gặp vấn đề
- Django authentication cần hiểu rõ để customize
- Signal tạo UserProfile tự động có thể gây lỗi

---

#### 📌 SPRINT 2 - Quản lý sách cơ bản (Tuần 3-4)

**🎯 Sprint Goal:** Người dùng có thể đăng và xem sách

| US ID | User Story | Story Points |
|-------|------------|--------------|
| US04 | Đăng bán sách | 8 |
| US05 | Xem danh sách sách | 5 |
| US07 | Xem chi tiết sách | 3 |
| **Total** | | **16 SP** |

**📋 Lý do sắp xếp:**
- Đây là tính năng cốt lõi của ứng dụng
- US04 có điểm cao nhất vì phức tạp nhất (form, upload ảnh, validation)
- US05 và US07 đi cùng vì liên quan chặt chẽ

**⚠️ Rủi ro:**
- Upload ảnh có thể gặp vấn đề về storage, kích thước
- Pagination cần test kỹ với dữ liệu lớn
- Performance với select_related/prefetch_related

---

#### 📌 SPRINT 3 - Tìm kiếm & Quản lý bài đăng (Tuần 5-6)

**🎯 Sprint Goal:** Tìm kiếm thông minh và quản lý bài đăng

| US ID | User Story | Story Points |
|-------|------------|--------------|
| US06 | Tìm kiếm và lọc sách | 5 |
| US08 | Chỉnh sửa/Xóa bài đăng | 3 |
| US14 | Xem thông tin liên hệ | 2 |
| **Total** | | **10 SP** |

**📋 Lý do sắp xếp:**
- Tìm kiếm nâng cao trải nghiệm người dùng
- Sửa/Xóa là tính năng cần thiết sau khi đăng
- Thông tin liên hệ kết hợp với chi tiết sách

**⚠️ Rủi ro:**
- Search query có thể chậm nếu không optimize index
- Phân quyền sửa/xóa cần test kỹ
- Privacy concern với thông tin liên hệ

---

#### 📌 SPRINT 4 - Giao dịch (Tuần 7-8)

**🎯 Sprint Goal:** Hoàn thiện quy trình mua bán

| US ID | User Story | Story Points |
|-------|------------|--------------|
| US09 | Gửi yêu cầu mua sách | 5 |
| US10 | Duyệt/Từ chối yêu cầu | 5 |
| US11 | Xem sách đã mua | 3 |
| **Total** | | **13 SP** |

**📋 Lý do sắp xếp:**
- Đây là luồng nghiệp vụ quan trọng nhất
- Cần thực hiện tuần tự: Gửi → Duyệt → Xem đã mua
- Liên quan đến thay đổi trạng thái sách

**⚠️ Rủi ro:**
- Logic duyệt yêu cầu phức tạp (auto-reject các request khác)
- Cần test kỹ flow: pending → approved/rejected
- Edge case: nhiều người gửi request cùng lúc

---

#### 📌 SPRINT 5 - Đánh giá & Hoàn thiện (Tuần 9-10)

**🎯 Sprint Goal:** Hệ thống đánh giá và hoàn thiện sản phẩm

| US ID | User Story | Story Points |
|-------|------------|--------------|
| US12 | Đánh giá người bán | 5 |
| US13 | Xem đánh giá | 3 |
| - | Testing & Bug fixes | 5 |
| - | Documentation | 3 |
| **Total** | | **16 SP** |

**📋 Lý do sắp xếp:**
- Đánh giá là tính năng cuối cùng theo dependency
- Cần giao dịch hoàn tất mới đánh giá được
- Sprint cuối dành cho testing và hoàn thiện

**⚠️ Rủi ro:**
- Logic kiểm tra quyền đánh giá phức tạp
- Cần test thoroughly để tránh fake review
- Performance với nhiều đánh giá

---

### 4.2 Tổng quan Sprint Planning

```
┌────────────────────────────────────────────────────────────────────────┐
│                     SPRINT OVERVIEW                                     │
├────────────────────────────────────────────────────────────────────────┤
│ Sprint │ Theme              │ US Count │ Story Points │ Status        │
├────────┼────────────────────┼──────────┼──────────────┼───────────────┤
│ SP1    │ Foundation         │ 3        │ 13 SP        │ ✅ Complete   │
│ SP2    │ Book Management    │ 3        │ 16 SP        │ ✅ Complete   │
│ SP3    │ Search & Edit      │ 3        │ 10 SP        │ ✅ Complete   │
│ SP4    │ Transaction        │ 3        │ 13 SP        │ ✅ Complete   │
│ SP5    │ Rating & Polish    │ 4        │ 16 SP        │ ✅ Complete   │
├────────┴────────────────────┴──────────┼──────────────┼───────────────┤
│ TOTAL                                  │ 68 SP        │ 100% Done     │
└────────────────────────────────────────┴──────────────┴───────────────┘
```

### 4.3 Đánh giá tiến độ hiện tại

**🎉 KẾT LUẬN: Dự án đã HOÀN THÀNH 100%**

Dựa trên phân tích source code, tất cả 14 User Stories đã được implement:

| Module | Chức năng | Status |
|--------|-----------|--------|
| Users | Đăng ký, Đăng nhập, Đăng xuất, Profile, Đổi mật khẩu | ✅ |
| Books | CRUD sách, Tìm kiếm, Lọc, Phân trang | ✅ |
| Purchase | Gửi yêu cầu, Duyệt, Từ chối, Sách đã mua | ✅ |
| Ratings | Đánh giá, Xem đánh giá, Tính điểm uy tín | ✅ |
| Tests | 40+ test cases covering tất cả flows | ✅ |

---

## 5. PHÂN RÃ TASK CHI TIẾT

### 5.1 US01 - Đăng ký tài khoản (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T01-01 | Tạo UserProfile model với các field bắt buộc | Database | 1h | Backend Dev |
| T01-02 | Viết UserRegisterForm với validation | Backend | 1.5h | Backend Dev |
| T01-03 | Tạo signal tự động tạo UserProfile | Backend | 0.5h | Backend Dev |
| T01-04 | Tạo template đăng ký responsive | Frontend | 1h | Frontend Dev |
| T01-05 | Implement view RegisterView | Backend | 0.5h | Backend Dev |
| T01-06 | Unit test đăng ký (success, fail, duplicate) | Testing | 1h | Tester |
| T01-07 | Review code và merge | Review | 0.5h | Team |

### 5.2 US02 - Đăng nhập/Đăng xuất (3 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T02-01 | Tạo template login với Bootstrap | Frontend | 0.5h | Frontend Dev |
| T02-02 | Implement user_login view | Backend | 1h | Backend Dev |
| T02-03 | Implement user_logout view | Backend | 0.25h | Backend Dev |
| T02-04 | Cấu hình LOGIN_REDIRECT_URL | Backend | 0.25h | Backend Dev |
| T02-05 | Unit test authentication | Testing | 0.5h | Tester |

### 5.3 US03 - Quản lý hồ sơ cá nhân (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T03-01 | Tạo UserProfileForm | Backend | 1h | Backend Dev |
| T03-02 | Tạo UserUpdateForm | Backend | 0.5h | Backend Dev |
| T03-03 | Tạo ChangePasswordForm | Backend | 0.5h | Backend Dev |
| T03-04 | Template user_profile.html | Frontend | 1.5h | Frontend Dev |
| T03-05 | Template user_edit_profile.html | Frontend | 1h | Frontend Dev |
| T03-06 | Template user_change_password.html | Frontend | 0.5h | Frontend Dev |
| T03-07 | Unit test profile update | Testing | 0.5h | Tester |

### 5.4 US04 - Đăng bán sách (8 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T04-01 | Tạo Subject model | Database | 0.5h | Backend Dev |
| T04-02 | Tạo Book model với đầy đủ fields | Database | 1h | Backend Dev |
| T04-03 | Tạo BookImage model (multiple images) | Database | 0.5h | Backend Dev |
| T04-04 | Tạo BookForm với widgets tùy chỉnh | Backend | 1.5h | Backend Dev |
| T04-05 | Implement BookCreateView | Backend | 1h | Backend Dev |
| T04-06 | Template book_create.html | Frontend | 1.5h | Frontend Dev |
| T04-07 | Cấu hình MEDIA_ROOT và upload path | Backend | 0.5h | Backend Dev |
| T04-08 | Implement image upload và resize | Backend | 1h | Backend Dev |
| T04-09 | Unit test book creation | Testing | 1h | Tester |

### 5.5 US05 - Xem danh sách sách (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T05-01 | Tạo BookListView với pagination | Backend | 1.5h | Backend Dev |
| T05-02 | Optimize query với select_related | Backend | 0.5h | Backend Dev |
| T05-03 | Template book_list.html với grid layout | Frontend | 2h | Frontend Dev |
| T05-04 | Implement book card component | Frontend | 1h | Frontend Dev |
| T05-05 | Unit test pagination và filtering | Testing | 0.5h | Tester |

### 5.6 US06 - Tìm kiếm và lọc sách (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T06-01 | Tạo BookSearchForm | Backend | 1h | Backend Dev |
| T06-02 | Implement search query (Q objects) | Backend | 1h | Backend Dev |
| T06-03 | Implement filters (subject, condition, price) | Backend | 1h | Backend Dev |
| T06-04 | Implement sorting options | Backend | 0.5h | Backend Dev |
| T06-05 | Update template với search bar và filters | Frontend | 1h | Frontend Dev |
| T06-06 | Unit test search và filter | Testing | 0.5h | Tester |

### 5.7 US07 - Xem chi tiết sách (3 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T07-01 | Tạo BookDetailView | Backend | 0.5h | Backend Dev |
| T07-02 | Implement increment_view_count | Backend | 0.25h | Backend Dev |
| T07-03 | Template book_detail.html | Frontend | 1.5h | Frontend Dev |
| T07-04 | Hiển thị sách tương tự | Backend | 0.5h | Backend Dev |
| T07-05 | Unit test book detail view | Testing | 0.25h | Tester |

### 5.8 US08 - Chỉnh sửa/Xóa bài đăng (3 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T08-01 | Tạo BookUpdateView với phân quyền | Backend | 0.5h | Backend Dev |
| T08-02 | Tạo BookDeleteView với confirmation | Backend | 0.5h | Backend Dev |
| T08-03 | Template book_update.html | Frontend | 0.5h | Frontend Dev |
| T08-04 | Template book_delete.html (modal) | Frontend | 0.5h | Frontend Dev |
| T08-05 | Unit test authorization | Testing | 0.5h | Tester |

### 5.9 US09 - Gửi yêu cầu mua sách (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T09-01 | Tạo PurchaseRequest model | Database | 1h | Backend Dev |
| T09-02 | Implement create_purchase_request view | Backend | 1.5h | Backend Dev |
| T09-03 | Add validation (không mua sách mình, sách đã bán) | Backend | 1h | Backend Dev |
| T09-04 | Template hiển thị request status | Frontend | 0.5h | Frontend Dev |
| T09-05 | Unit test purchase request creation | Testing | 1h | Tester |

### 5.10 US10 - Duyệt/Từ chối yêu cầu mua (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T10-01 | Implement approve_purchase_request | Backend | 1h | Backend Dev |
| T10-02 | Implement reject_purchase_request | Backend | 0.5h | Backend Dev |
| T10-03 | Implement auto-reject logic | Backend | 1h | Backend Dev |
| T10-04 | Template my_books với pending requests | Frontend | 1.5h | Frontend Dev |
| T10-05 | Template my_purchase_requests | Frontend | 1h | Frontend Dev |
| T10-06 | Unit test approve/reject flow | Testing | 1h | Tester |

### 5.11 US11 - Xem sách đã mua (3 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T11-01 | Tạo purchased_books view | Backend | 1h | Backend Dev |
| T11-02 | Template purchased_books.html | Frontend | 1h | Frontend Dev |
| T11-03 | Add has_rated annotation | Backend | 0.5h | Backend Dev |
| T11-04 | Unit test purchased books | Testing | 0.5h | Tester |

### 5.12 US12 - Đánh giá người bán (5 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T12-01 | Tạo Rating model | Database | 0.5h | Backend Dev |
| T12-02 | Tạo RatingForm | Backend | 0.5h | Backend Dev |
| T12-03 | Implement create_rating view với validation | Backend | 1.5h | Backend Dev |
| T12-04 | Implement update_reputation trong UserProfile | Backend | 1h | Backend Dev |
| T12-05 | Template rating_create.html | Frontend | 1h | Frontend Dev |
| T12-06 | Unit test rating logic | Testing | 1h | Tester |

### 5.13 US13 - Xem đánh giá người bán (3 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T13-01 | Tạo user_ratings view | Backend | 1h | Backend Dev |
| T13-02 | Template rating_list.html | Frontend | 1h | Frontend Dev |
| T13-03 | Hiển thị thống kê đánh giá | Frontend | 0.5h | Frontend Dev |
| T13-04 | Unit test rating display | Testing | 0.25h | Tester |

### 5.14 US14 - Xem thông tin liên hệ (2 SP)

| Task ID | Task | Type | Estimate | Assignee |
|---------|------|------|----------|----------|
| T14-01 | Thêm seller_contact_info property | Backend | 0.5h | Backend Dev |
| T14-02 | Hiển thị thông tin liên hệ trong book_detail | Frontend | 0.5h | Frontend Dev |
| T14-03 | Template user_profile với contact info | Frontend | 0.5h | Frontend Dev |

---

## 6. HƯỚNG DẪN TẠO SPRINT TRONG JIRA

### 6.1 Thiết lập Project

1. **Tạo Project mới**
   - Chọn "Scrum" template
   - Đặt tên: "DUE Book - Book Exchange Platform"
   - Key: `DUE`

2. **Cấu hình Issue Types**
   ```
   - Epic: Module (Users, Books, Ratings)
   - Story: User Story (US01-US14)
   - Task: Technical Task (T01-01, T01-02...)
   - Sub-task: Chi tiết nhỏ hơn
   - Bug: Lỗi phát hiện
   ```

3. **Tạo Custom Fields**
   - Story Points (Number)
   - Priority (Select: High, Medium, Low)
   - Module (Select: Users, Books, Purchase, Ratings)

### 6.2 Tạo User Stories

Template tạo Issue:

```
Summary: [US01] Đăng ký tài khoản mới
Issue Type: Story
Description:
  AS A Sinh viên mới
  I WANT TO Đăng ký tài khoản với thông tin liên hệ
  SO THAT Có thể tham gia mua bán trên hệ thống
  
  Acceptance Criteria:
  - Form đăng ký gồm: username, email, password, họ tên
  - Bắt buộc nhập số điện thoại, link Facebook, link Zalo
  - Validate trùng username
  - Validate mật khẩu xác nhận
  
Story Points: 5
Priority: High
Module: Users
Epic Link: Users Module
```

### 6.3 Tạo Sprints

**Tạo Sprint 1:**
1. Vào Backlog
2. Click "Create Sprint"
3. Đặt tên: "Sprint 1 - Foundation & Authentication"
4. Set Start Date và End Date (2 tuần)
5. Add User Stories: US01, US02, US03
6. Click "Start Sprint"

**Sprint Goal Example:**
```
Thiết lập nền tảng dự án và hệ thống authentication.
User có thể đăng ký, đăng nhập và quản lý hồ sơ.
```

### 6.4 Tạo Tasks cho mỗi Story

Ví dụ cho US01:
```
Parent: US01 - Đăng ký tài khoản
Tasks:
├── T01-01: Tạo UserProfile model [Backend]
├── T01-02: Viết UserRegisterForm [Backend]
├── T01-03: Tạo signal tự động tạo UserProfile [Backend]
├── T01-04: Tạo template đăng ký [Frontend]
├── T01-05: Implement RegisterView [Backend]
├── T01-06: Unit test đăng ký [Testing]
└── T01-07: Review code [Review]
```

### 6.5 Workflow Status

```
TO DO → IN PROGRESS → IN REVIEW → DONE
         ↓
      BLOCKED
```

---

## 7. CÁCH THEO DÕI BURNDOWN CHART

### 7.1 Burndown Chart là gì?

Burndown Chart hiển thị lượng công việc còn lại theo thời gian, giúp team:
- Theo dõi tiến độ sprint
- Dự đoán khả năng hoàn thành
- Phát hiện vấn đề sớm

### 7.2 Cách đọc Burndown Chart

```
Story Points
    │
80 ─┼────────────────────────────────────
    │ ╲
    │  ╲ Ideal Line (đường lý tưởng)
    │   ╲
60 ─┼────╲───────────────────────────────
    │     ╲
    │      ╲
40 ─┼───────╲────────────────────────────
    │        ╲ Actual Line (đường thực tế)
    │         ╲╱╲
20 ─┼───────────╲────────────────────────
    │            ╲
    │             ╲
 0 ─┼──────────────╲─────────────────────
    │  Day1 Day5 Day10 Day15 (Sprint Days)
```

**Đọc hiểu:**
- **Ideal Line:** Đường chéo từ tổng SP xuống 0
- **Actual Line:** Đường thực tế công việc còn lại
- **Nếu Actual > Ideal:** Team đang chậm tiến độ
- **Nếu Actual < Ideal:** Team đang nhanh hơn dự kiến

### 7.3 Cập nhật hàng ngày

**Daily Standup format:**
```
1. Hôm qua tôi làm gì? (Update task status)
2. Hôm nay tôi sẽ làm gì? (Move task to In Progress)
3. Có vấn đề gì không? (Blockers)
```

**Update Jira:**
1. Log work vào task
2. Update Remaining Estimate
3. Move task giữa các status
4. Comment nếu có vấn đề

### 7.4 Velocity Calculation

```
Velocity = Tổng Story Points hoàn thành / Sprint

Sprint 1: 13 SP → Velocity = 13
Sprint 2: 16 SP → Velocity = 16
Sprint 3: 10 SP → Velocity = 10
Sprint 4: 13 SP → Velocity = 13
Sprint 5: 16 SP → Velocity = 16

Average Velocity = (13+16+10+13+16) / 5 = 13.6 SP/Sprint
```

### 7.5 Sprint Metrics

| Metric | Công thức | Mục tiêu |
|--------|-----------|----------|
| Sprint Burndown | SP còn lại / Tổng SP | Về 0 cuối sprint |
| Velocity | SP hoàn thành / Sprint | Ổn định hoặc tăng |
| Cycle Time | Ngày từ In Progress → Done | < 5 ngày |
| Lead Time | Ngày từ To Do → Done | < 10 ngày |

---

## 8. CHECKLIST TRƯỚC KHI REVIEW SPRINT

### 8.1 Checklist cho Developer

#### Code Quality
- [ ] Code tuân theo PEP 8 (Python)
- [ ] Không có hardcoded values
- [ ] Comments đầy đủ cho các hàm phức tạp
- [ ] Đặt tên biến/hàm có ý nghĩa
- [ ] Không có dead code

#### Testing
- [ ] Unit tests pass 100%
- [ ] Coverage > 80%
- [ ] Integration tests pass
- [ ] Manual test trên local

#### Documentation
- [ ] Docstring cho models, views, forms
- [ ] README update nếu cần
- [ ] API documentation (nếu có)

### 8.2 Checklist cho Sprint Review

#### Chuẩn bị
- [ ] Tất cả User Stories trong Sprint đã DONE
- [ ] Demo environment sẵn sàng
- [ ] Test data đã chuẩn bị
- [ ] Slides demo (nếu cần)

#### Nội dung Review
- [ ] Sprint Goal achieved?
- [ ] Demo từng User Story
- [ ] Metrics: Velocity, Burndown
- [ ] Issues encountered & Solutions
- [ ] Feedback từ Product Owner

#### Handoff
- [ ] Code đã merge vào main branch
- [ ] Database migrations đã chạy
- [ ] Static files đã collect
- [ ] Production deployment plan

### 8.3 Checklist cho Sprint Retrospective

#### What went well?
- [ ] Ghi nhận những điểm tốt
- [ ] Best practices để maintain

#### What could be improved?
- [ ] Điểm cần cải thiện
- [ ] Root cause analysis

#### Action Items
- [ ] Cụ thể, đo lường được
- [ ] Assign owner
- [ ] Set deadline

### 8.4 Definition of Done (DoD)

Một User Story được coi là **DONE** khi:

```
□ Code hoàn thành và self-reviewed
□ Code reviewed bởi peer
□ Unit tests viết và pass
□ Integration tests pass
□ Acceptance Criteria met
□ Product Owner approval
□ Documentation updated
□ Deployed to staging
□ No critical bugs
```

---

## PHỤ LỤC

### A. Tham chiếu nhanh

| Lệnh | Mô tả |
|------|-------|
| `python manage.py runserver` | Chạy development server |
| `python manage.py test` | Chạy tất cả tests |
| `python manage.py test books` | Chạy tests của module books |
| `python manage.py migrate` | Chạy database migrations |
| `python manage.py createsuperuser` | Tạo admin user |
| `python manage.py collectstatic` | Collect static files |

### B. Liên hệ hỗ trợ

| Vai trò | Người phụ trách |
|---------|-----------------|
| Product Owner | [Tên] |
| Scrum Master | [Tên] |
| Tech Lead | [Tên] |
| Backend Dev | [Tên] |
| Frontend Dev | [Tên] |
| Tester | [Tên] |

### C. Tài liệu tham khảo

- [Django Documentation](https://docs.djangoproject.com/)
- [Scrum Guide](https://scrumguides.org/)
- [Atlassian Agile Coach](https://www.atlassian.com/agile)

---

*Tài liệu này được tạo tự động bởi Cline AI Assistant*
*Last updated: 22/02/2026*