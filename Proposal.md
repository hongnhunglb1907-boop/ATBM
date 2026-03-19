# DUE BOOK - PROJECT PROPOSAL
## Website Mua Bán Sách Dành Riêng Cho Sinh Viên DUE

---

# TÀI LIỆU QUẢN TRỊ DỰ ÁN AGILE/SCRUM

> **Đơn vị phát triển:** Nhóm sinh viên 49K212.06  
> **Khóa:** K212 - Đại học Kinh tế - ĐHĐN  
> **Ngày tạo tài liệu:** 22/02/2026  
> **Phiên bản:** 1.0

---

## MỤC LỤC

1. [Tổng quan dự án](#1-tổng-quan-dự-án)
2. [Phạm vi dự án](#2-phạm-vi-dự-án)
3. [Yêu cầu chức năng](#3-yêu-cầu-chức-năng)
4. [Product Backlog](#4-product-backlog)
5. [Phân tích Dependency](#5-phân-tích-dependency)
6. [MASTER SCHEDULE](#6-master-schedule)
7. [Phân công nguồn lực](#7-phân-công-nguồn-lực)
8. [Quản lý rủi ro](#8-quản-lý-rủi-ro)

---

## 1. TỔNG QUAN DỰ ÁN

### 1.1 Giới thiệu

**DUE Book** là nền tảng mua bán và trao đổi sách cũ dành riêng cho sinh viên Đại học Kinh tế (DUE) - Đại học Đà Nẵng. Hệ thống cung cấp giải pháp kết nối người bán và người mua sách cũ trong nội trường, giúp sinh viên tiết kiệm chi phí học tập và tối ưu hóa vòng đời của sách.

### 1.2 Mục tiêu dự án

| STT | Mục tiêu | Mô tả chi tiết |
|-----|----------|----------------|
| 1 | **Kết nối** | Xây dựng cộng đồng mua bán sách trong trường |
| 2 | **Tiết kiệm** | Giúp sinh viên giảm 50-80% chi phí mua sách |
| 3 | **Minh bạch** | Hệ thống đánh giá uy tín người bán |
| 4 | **Tiện lợi** | Giao diện thân thiện, dễ sử dụng |
| 5 | **Bảo mật** | Thông tin cá nhân được bảo vệ |

### 1.3 Công nghệ áp dụng

| Thành phần | Công nghệ | Phiên bản |
|------------|-----------|-----------|
| Backend Framework | Django | 5.x |
| Frontend Framework | Bootstrap | 5.x |
| Ngôn ngữ lập trình | Python | 3.10+ |
| Cơ sở dữ liệu | SQLite / PostgreSQL | 3.x / 15.x |
| Hệ điều hành | Windows / Linux | - |
| Hệ thống kiểm thử | Django TestCase | - |

---

## 2. PHẠM VI DỰ ÁN

### 2.1 Phạm vi In-Scope

**Module Users - Quản lý người dùng:**
- Đăng ký tài khoản với thông tin liên hệ
- Đăng nhập / Đăng xuất
- Quản lý hồ sơ cá nhân
- Đổi mật khẩu
- Xem thông tin liên hệ

**Module Books - Quản lý sách:**
- Đăng bán sách với đầy đủ thông tin
- Xem danh sách sách (phân trang)
- Xem chi tiết sách
- Tìm kiếm và lọc sách theo tiêu chí
- Chỉnh sửa / Xóa bài đăng
- Quản lý sách cá nhân

**Module Purchase Request - Yêu cầu mua:**
- Gửi yêu cầu mua sách
- Duyệt / Từ chối yêu cầu
- Xem sách đã mua thành công

**Module Ratings - Đánh giá:**
- Đánh giá người bán sau giao dịch
- Xem đánh giá của người bán
- Tính toán điểm uy tín tự động

### 2.2 Phạm vi Out-of-Scope

- Thanh toán trực tuyến
- Giao hàng vận chuyển
- Mobile Application (Native)
- Chat realtime
- Thông báo push notification
- Quảng cáo và khuyến mãi

---

## 3. YÊU CẦU CHỨC NĂNG

### 3.1 Danh sách User Stories

| ID | User Story | Priority | Story Points | Module |
|----|------------|----------|--------------|--------|
| **US01** | Đăng ký tài khoản mới | **High** | 5 | Users |
| **US02** | Đăng nhập vào hệ thống | **High** | 3 | Users |
| **US03** | Quản lý hồ sơ cá nhân | Medium | 5 | Users |
| **US04** | Đăng bán sách | **High** | 8 | Books |
| **US05** | Xem danh sách sách | **High** | 5 | Books |
| **US06** | Tìm kiếm và lọc sách | **High** | 5 | Books |
| **US07** | Xem chi tiết sách | **High** | 3 | Books |
| **US08** | Chỉnh sửa/Xóa bài đăng | Medium | 3 | Books |
| **US09** | Gửi yêu cầu mua sách | **High** | 5 | Purchase |
| **US10** | Duyệt/Từ chối yêu cầu mua | **High** | 5 | Purchase |
| **US11** | Xem sách đã mua | Medium | 3 | Purchase |
| **US12** | Đánh giá người bán | Medium | 5 | Ratings |
| **US13** | Xem đánh giá người bán | Low | 3 | Ratings |
| **US14** | Xem thông tin liên hệ | Medium | 2 | Users |

### 3.2 Chi tiết Acceptance Criteria

#### US01 - Đăng ký tài khoản mới (Priority: High - 5 SP)
```
AS A Sinh viên mới
I WANT TO Đăng ký tài khoản với thông tin liên hệ
SO THAT Có thể tham gia mua bán trên hệ thống

ACCEPTANCE CRITERIA:
✓ Form đăng ký gồm: username, email, password, họ tên
✓ Bắt buộc nhập số điện thoại, link Facebook, link Zalo
✓ Validate trùng username
✓ Validate mật khẩu xác nhận
✓ Tự động tạo UserProfile sau khi đăng ký
```

#### US02 - Đăng nhập vào hệ thống (Priority: High - 3 SP)
```
AS A Người dùng đã có tài khoản
I WANT TO Đăng nhập với username/password
SO THAT Truy cập các chức năng của hệ thống

ACCEPTANCE CRITERIA:
✓ Form đăng nhập với username, password
✓ Hiển thị thông báo lỗi khi sai thông tin
✓ Redirect đến trang yêu cầu sau khi login
✓ Lưu session đăng nhập
```

#### US03 - Quản lý hồ sơ cá nhân (Priority: Medium - 5 SP)
```
AS A Người dùng đã đăng nhập
I WANT TO Xem và chỉnh sửa thông tin cá nhân
SO THAT Cập nhật thông tin liên hệ, avatar

ACCEPTANCE CRITERIA:
✓ Xem được hồ sơ của mình và người khác
✓ Chỉnh sửa được: avatar, bio, phone, facebook, zalo
✓ Đổi được mật khẩu
✓ Hiển thị thống kê: số sách đã bán, điểm uy tín
```

#### US04 - Đăng bán sách (Priority: High - 8 SP)
```
AS A Sinh viên có sách cũ
I WANT TO Đăng bài bán sách với đầy đủ thông tin
SO THAT Người khác có thể tìm và mua sách

ACCEPTANCE CRITERIA:
✓ Form gồm: tên sách, tác giả, môn học, giá bán, giá bìa
✓ Chọn tình trạng sách (Mới, Like new, Khá, Trung bình, Cũ)
✓ Upload ảnh bìa
✓ Tự động hiển thị thông tin liên hệ từ UserProfile
✓ Validate giá tối thiểu 1,000 VNĐ
```

#### US09 - Gửi yêu cầu mua sách (Priority: High - 5 SP)
```
AS A Người mua
I WANT TO Gửi yêu cầu mua sách
SO THAT Người bán biết tôi muốn mua

ACCEPTANCE CRITERIA:
✓ Nút "Tôi đã mua sách này" trên trang chi tiết
✓ Không thể mua sách của chính mình
✓ Không thể mua sách đã bán
✓ Mỗi user chỉ gửi 1 yêu cầu cho 1 sách
✓ Status mặc định là PENDING
```

#### US10 - Duyệt/Từ chối yêu cầu mua (Priority: High - 5 SP)
```
AS A Người bán
I WANT TO Duyệt hoặc từ chối yêu cầu mua
SO THAT Xác nhận giao dịch với người mua phù hợp

ACCEPTANCE CRITERIA:
✓ Xem danh sách yêu cầu đang chờ
✓ Duyệt → Book.status = 'sold', Book.buyer = buyer
✓ Từ chối → Request.status = 'rejected'
✓ Khi duyệt 1 request, các request khác tự động rejected
```

---

## 4. PRODUCT BACKLOG

### 4.1 Product Backlog theo Priority

#### 🔴 HIGH PRIORITY (Phải hoàn thành trước)

| ID | User Story | Story Points | Module | Dependencies |
|----|------------|--------------|--------|--------------|
| US01 | Đăng ký tài khoản | 5 | Users | None |
| US02 | Đăng nhập hệ thống | 3 | Users | US01 |
| US04 | Đăng bán sách | 8 | Books | US02 |
| US05 | Xem danh sách sách | 5 | Books | None |
| US06 | Tìm kiếm và lọc sách | 5 | Books | US05 |
| US07 | Xem chi tiết sách | 3 | Books | US05 |
| US09 | Gửi yêu cầu mua | 5 | Purchase | US02, US07 |
| US10 | Duyệt yêu cầu mua | 5 | Purchase | US09 |
| **Total High** | **8 items** | **39 SP** | | |

#### 🟡 MEDIUM PRIORITY (Hoàn thành sau High)

| ID | User Story | Story Points | Module | Dependencies |
|----|------------|--------------|--------|--------------|
| US03 | Quản lý hồ sơ | 5 | Users | US02 |
| US08 | Sửa/Xóa bài đăng | 3 | Books | US04 |
| US11 | Xem sách đã mua | 3 | Purchase | US10 |
| US12 | Đánh giá người bán | 5 | Ratings | US10, US11 |
| US14 | Thông tin liên hệ | 2 | Users | US07 |
| **Total Medium** | **5 items** | **18 SP** | | |

#### 🟢 LOW PRIORITY (Làm nếu có thời gian)

| ID | User Story | Story Points | Module | Dependencies |
|----|------------|--------------|--------|--------------|
| US13 | Xem đánh giá | 3 | Ratings | US12 |
| **Total Low** | **1 item** | **3 SP** | | |

### 4.2 Tổng hợp Product Backlog

| Priority | Số User Stories | Tổng Story Points |
|----------|-----------------|-------------------|
| **High** | 8 | 39 SP |
| **Medium** | 5 | 18 SP |
| **Low** | 1 | 3 SP |
| **TOTAL** | **14** | **60 SP** |

---

## 5. PHÂN TÍCH DEPENDENCY

### 5.1 Dependency Graph

```
                        ┌──────────────────┐
                        │   US01 Đăng ký    │
                        │   (High - 5 SP)   │
                        └─────────┬────────┘
                                  │
                        ┌─────────▼────────┐
                        │  US02 Đăng nhập   │
                        │   (High - 3 SP)   │
                        └─────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
    ┌─────────▼────────┐ ┌───────▼────────┐ ┌───────▼────────┐
    │  US03 Profile    │ │  US04 Đăng bán │ │  US05 Danh sách│
    │ (Medium - 5 SP)  │ │  (High - 8 SP) │ │  (High - 5 SP) │
    └──────────────────┘ └───────┬────────┘ └───────┬────────┘
                                  │                   │
                        ┌─────────▼────────┐ ┌───────▼────────┐
                        │  US08 Sửa/Xóa    │ │  US06 Tìm kiếm │
                        │ (Medium - 3 SP)  │ │  (High - 5 SP) │
                        └──────────────────┘ └───────┬────────┘
                                                  │
                                        ┌─────────▼────────┐
                                        │  US07 Chi tiết   │
                                        │  (High - 3 SP)   │
                                        └─────────┬────────┘
                                                  │
                          ┌───────────────────────┼───────────────────────┐
                          │                       │                       │
                ┌─────────▼────────┐    ┌────────▼────────┐    ┌────────▼────────┐
                │  US09 Gửi yêu cầu│    │  US14 Liên hệ   │    │  US11 Đã mua    │
                │  (High - 5 SP)   │    │ (Medium - 2 SP) │    │ (Medium - 3 SP) │
                └─────────┬────────┘    └─────────────────┘    └────────┬────────┘
                          │                                            │
                ┌─────────▼────────┐                                  │
                │  US10 Duyệt yêu  │                                  │
                │  (High - 5 SP)   │                                  │
                └─────────┬────────┘                                  │
                          │                                           │
                ┌─────────▼──────────────────────────────────────────▼┐
                │                    US12 Đánh giá                     │
                │                  (Medium - 5 SP)                     │
                └─────────┬────────────────────────────────────────────┘
                          │
                ┌─────────▼────────┐
                │  US13 Xem đánh giá│
                │   (Low - 3 SP)    │
                └──────────────────┘
```

### 5.2 Dependency Rules (Quy tắc phụ thuộc)

| Quy tắc | Mô tả | Lý do |
|---------|-------|-------|
| **Rule 1** | Authentication trước tất cả | Phải có user mới thực hiện được chức năng |
| **Rule 2** | Posting trước Search | Cần có dữ liệu sách mới tìm kiếm được |
| **Rule 3** | Posting + User trước Rating | Cần giao dịch thành công mới đánh giá được |
| **Rule 4** | Detail trước Purchase | Phải xem chi tiết mới mua được |
| **Rule 5** | Approve trước Rating | Phải hoàn thành giao dịch mới đánh giá |

---

## 6. MASTER SCHEDULE

### 6.1 Thông tin dự án

| Thông số | Giá trị |
|----------|---------|
| **Ngày bắt đầu** | 01/03/2026 |
| **Ngày kết thúc** | 12/04/2026 |
| **Tổng thời gian** | 43 ngày (6 tuần + 1 ngày) |
| **Số Sprint** | 6 Sprint |
| **Độ dài Sprint** | 1 tuần/Sprint |
| **Team size** | 6 người |
| **Giờ làm việc** | 3 giờ/ngày |
| **Số ngày làm việc/tuần** | 5 ngày |

### 6.2 Tính toán năng lực Team

**Năng lực Sprint:**
```
Số giờ làm việc/Sprint = 6 người × 3 giờ/ngày × 5 ngày = 90 giờ/Sprint
Efficiency Factor = 0.7 (trừ meetings, reviews, overheads)
Effective Hours = 90 × 0.7 = 63 giờ/Sprint
```

**Velocity ước tính:**
```
Average Story Points/Sprint = 10-15 SP (dựa trên complexity)
```

### 6.3 Bảng MASTER SCHEDULE

| Sprint | Thời gian | Số tuần | Mục tiêu chính (Goal) | Mô tả công việc tổng quát |
|--------|-----------|---------|----------------------|---------------------------|
| **Sprint 1** | 01/03/2026 - 07/03/2026 | 1 tuần | **Thiết lập nền tảng & Authentication** | • Thiết lập môi trường development (Django, Database, Git) <br>• Cấu trúc dự án Django (apps, settings, urls) <br>• **US01**: Đăng ký tài khoản (Model UserProfile, Form, View, Template) <br>• **US02**: Đăng nhập/Đăng xuất (Authentication views, Session) <br>• Unit test authentication (signup, login, logout) <br>• Code review & Documentation |
| **Sprint 2** | 08/03/2026 - 14/03/2026 | 1 tuần | **Module Book - Đăng và Xem sách** | • **US04**: Đăng bán sách (Book model, Subject model, BookForm, Image upload) <br>• **US05**: Xem danh sách sách (BookListView, Pagination, Grid layout) <br>• **US07**: Xem chi tiết sách (BookDetailView, View count, Related books) <br>• Cấu hình MEDIA_ROOT, static files <br>• Unit test Book CRUD operations |
| **Sprint 3** | 15/03/2026 - 21/03/2026 | 1 tuần | **Tìm kiếm & Quản lý bài đăng** | • **US06**: Tìm kiếm và lọc sách (SearchForm, Q objects, Filters, Sorting) <br>• **US03**: Quản lý hồ sơ cá nhân (ProfileView, EditProfile, ChangePassword) <br>• **US08**: Chỉnh sửa/Xóa bài đăng (BookUpdateView, BookDeleteView, Authorization) <br>• **US14**: Xem thông tin liên hệ (Seller contact display) <br>• Unit test Search, Filter, Profile |
| **Sprint 4** | 22/03/2026 - 28/03/2026 | 1 tuần | **Quy trình giao dịch (Purchase Flow)** | • **US09**: Gửi yêu cầu mua sách (PurchaseRequest model, Validation, Create view) <br>• **US10**: Duyệt/Từ chối yêu cầu (Approve/Reject views, Auto-reject logic, Status change) <br>• **US11**: Xem sách đã mua (PurchasedBooksView, Transaction history) <br>• Purchase flow integration test <br>• UI/UX improvement cho purchase workflow |
| **Sprint 5** | 29/03/2026 - 04/04/2026 | 1 tuần | **Hệ thống đánh giá & Hoàn thiện UI** | • **US12**: Đánh giá người bán (Rating model, RatingForm, Validation, Reputation calculation) <br>• **US13**: Xem đánh giá người bán (RatingListView, Statistics) <br>• Hoàn thiện UI/UX (Responsive design, Error pages, Loading states) <br>• Performance optimization (select_related, prefetch_related) <br>• Unit test Rating functionality |
| **Sprint 6** | 05/04/2026 - 12/04/2026 | 1 tuần + 1 ngày | **Testing, UAT & Chuẩn bị Demo** | • **Integration Test**: End-to-end testing toàn bộ flows <br>• **UAT (User Acceptance Testing)**: Test với end users thực tế <br>• **Bug Fixing**: Sửa lỗi phát hiện trong UAT <br>• **Code Refactoring**: Clean code, optimize queries <br>• **Documentation**: README, API docs, User guide <br>• **Demo Preparation**: Slide thuyết trình (8-10 slides) <br>• **Demo Script**: Kịch bản demo sản phẩm <br>• **Final Deployment**: Deploy lên staging/production |

### 6.4 Chi tiết từng Sprint

#### 📌 SPRINT 1 - Nền tảng & Authentication
**Thời gian:** 01/03/2026 - 07/03/2026

| User Story | Story Points | Tasks |
|------------|--------------|-------|
| US01 - Đăng ký | 5 SP | T01-01 đến T01-07 |
| US02 - Đăng nhập | 3 SP | T02-01 đến T02-05 |
| Setup Project | - | Init Django, Database, Git |

**Deliverables:**
- ✅ Môi trường development hoạt động
- ✅ User có thể đăng ký tài khoản mới
- ✅ User có thể đăng nhập/đăng xuất
- ✅ Unit tests pass 100%

**Risks:**
- ⚠️ Môi trường development có thể gặp vấn đề
- ⚠️ Django authentication cần customize

---

#### 📌 SPRINT 2 - Module Book (Đăng & Xem)
**Thời gian:** 08/03/2026 - 14/03/2026

| User Story | Story Points | Tasks |
|------------|--------------|-------|
| US04 - Đăng bán sách | 8 SP | T04-01 đến T04-09 |
| US05 - Danh sách sách | 5 SP | T05-01 đến T05-05 |
| US07 - Chi tiết sách | 3 SP | T07-01 đến T07-05 |

**Deliverables:**
- ✅ User có thể đăng bán sách với ảnh
- ✅ User có thể xem danh sách sách (phân trang)
- ✅ User có thể xem chi tiết sách
- ✅ Database có subjects mẫu

**Risks:**
- ⚠️ Image upload cần validate size/format
- ⚠️ Pagination cần test với data lớn

---

#### 📌 SPRINT 3 - Tìm kiếm & Quản lý
**Thời gian:** 15/03/2026 - 21/03/2026

| User Story | Story Points | Tasks |
|------------|--------------|-------|
| US06 - Tìm kiếm lọc | 5 SP | T06-01 đến T06-06 |
| US03 - Hồ sơ cá nhân | 5 SP | T03-01 đến T03-07 |
| US08 - Sửa/Xóa bài | 3 SP | T08-01 đến T08-05 |
| US14 - Thông tin liên hệ | 2 SP | T14-01 đến T14-03 |

**Deliverables:**
- ✅ User có thể tìm kiếm, lọc, sắp xếp sách
- ✅ User có thể quản lý profile
- ✅ User có thể sửa/xóa bài đăng
- ✅ Thông tin liên hệ hiển thị đầy đủ

**Risks:**
- ⚠️ Search query cần optimize index
- ⚠️ Authorization cần test kỹ

---

#### 📌 SPRINT 4 - Purchase Flow
**Thời gian:** 22/03/2026 - 28/03/2026

| User Story | Story Points | Tasks |
|------------|--------------|-------|
| US09 - Gửi yêu cầu | 5 SP | T09-01 đến T09-05 |
| US10 - Duyệt yêu cầu | 5 SP | T10-01 đến T10-06 |
| US11 - Sách đã mua | 3 SP | T11-01 đến T11-04 |

**Deliverables:**
- ✅ User có thể gửi yêu cầu mua
- ✅ Seller có thể duyệt/từ chối
- ✅ User có thể xem sách đã mua
- ✅ Auto-reject logic hoạt động đúng

**Risks:**
- ⚠️ Logic approve/reject phức tạp
- ⚠️ Edge cases cần test kỹ

---

#### 📌 SPRINT 5 - Rating & UI Polish
**Thời gian:** 29/03/2026 - 04/04/2026

| User Story | Story Points | Tasks |
|------------|--------------|-------|
| US12 - Đánh giá | 5 SP | T12-01 đến T12-06 |
| US13 - Xem đánh giá | 3 SP | T13-01 đến T13-04 |
| UI/UX Polish | - | Responsive, Error pages |

**Deliverables:**
- ✅ User có thể đánh giá seller
- ✅ Điểm uy tín tự động cập nhật
- ✅ UI responsive trên mọi thiết bị
- ✅ Error handling hoàn thiện

**Risks:**
- ⚠️ Rating validation phức tạp
- ⚠️ Performance với nhiều ratings

---

#### 📌 SPRINT 6 - Testing, UAT & Demo
**Thời gian:** 05/04/2026 - 12/04/2026

| Activity | Duration | Description |
|----------|----------|-------------|
| Integration Testing | 2 days | End-to-end test all flows |
| UAT | 1.5 days | Testing với end users |
| Bug Fixing | 1.5 days | Sửa bugs từ UAT |
| Documentation | 0.5 day | README, User guide |
| Demo Prep | 1.5 days | Slide (8-10 slides), Script demo |

**Deliverables:**
- ✅ All integration tests pass
- ✅ UAT completed với user feedback
- ✅ Critical bugs fixed
- ✅ Documentation complete
- ✅ Demo slides (8-10 slides)
- ✅ Demo script
- ✅ Ready for final presentation

**Demo Slide Structure:**
1. Title & Team Introduction
2. Problem Statement
3. Solution - DUE Book
4. Key Features
5. Technical Architecture
6. Demo Walkthrough
7. Testing Results
8. Challenges & Solutions
9. Future Improvements
10. Q&A

---

### 6.5 Sprint Timeline Visualization

```
THÁNG 3/2026
┌─────────────────────────────────────────────────────────────────────┐
│  CN  T2   T3   T4   T5   T6   T7   CN  T2   T3   T4   T5   T6   T7 │
├─────────────────────────────────────────────────────────────────────┤
│   1   2    3    4    5    6    7    8   9   10   11   12   13   14 │
│  ├───SPRINT 1─────────────────┤├────SPRINT 2─────────────────────┤ │
│  │ Authentication & Setup     ││ Book Posting & Viewing          │ │
└─────────────────────────────────────────────────────────────────────┘
│  15  16   17   18   19   20   21   22  23   24   25   26   27   28 │
│  ├───SPRINT 3─────────────────┤├────SPRINT 4─────────────────────┤ │
│  │ Search & Management        ││ Purchase Flow                   │ │
└─────────────────────────────────────────────────────────────────────┘

THÁNG 4/2026
┌─────────────────────────────────────────────────────────────────────┐
│  CN  T2   T3   T4   T5   T6   T7   CN  T2   T3   T4   T5   T6   T7 │
├─────────────────────────────────────────────────────────────────────┤
│       1    2    3    4    5    6    7    8    9   10   11   12    │
│       ├───SPRINT 5─────────────────┤├────SPRINT 6─────────────────┤│
│       │ Rating & UI Polish         ││ Testing, UAT & Demo Prep    ││
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. PHÂN CÔNG NGUỒN LỰC

### 7.1 Team Composition

| Vai trò | Số lượng | Trách nhiệm |
|---------|----------|-------------|
| Product Owner | 1 | Quản lý Product Backlog, Acceptance |
| Scrum Master | 1 | Facilitate Scrum events, Remove blockers |
| Backend Developer | 2 | Django models, views, API logic |
| Frontend Developer | 1 | Templates, CSS, JavaScript |
| Tester | 1 | Unit test, Integration test, UAT |

### 7.2 Năng lực Team

```
Tổng giờ làm việc = 6 người × 3 giờ/ngày × 5 ngày/tuần = 90 giờ/tuần
Efficiency = 70% (trừ meetings, reviews)
Effective = 63 giờ/tuần
```

### 7.3 Sprint Velocity Projection

| Sprint | Planned SP | Expected Velocity |
|--------|------------|-------------------|
| Sprint 1 | 8 SP | 8 SP (learning curve) |
| Sprint 2 | 16 SP | 14 SP |
| Sprint 3 | 15 SP | 14 SP |
| Sprint 4 | 13 SP | 13 SP |
| Sprint 5 | 8 SP | 10 SP |
| **Total** | **60 SP** | **59 SP** |

---

## 8. QUẢN LÝ RỦI RO

### 8.1 Risk Register

| ID | Rủi ro | Probability | Impact | Mitigation Strategy |
|----|--------|-------------|--------|---------------------|
| R1 | Team chưa quen Django | Medium | High | Training session, Pair programming |
| R2 | Requirements thay đổi | High | Medium | Change control process, PO approval |
| R3 | Technical debt | Medium | Medium | Code review, Refactoring sprints |
| R4 | Resource unavailable | Low | High | Cross-training, Documentation |
| R5 | Integration issues | Medium | High | Early integration testing |
| R6 | Performance issues | Low | Medium | Query optimization, Caching |

### 8.2 Definition of Done (DoD)

Một User Story được coi là **DONE** khi:

```
□ Code hoàn thành và self-reviewed
□ Code reviewed bởi peer
□ Unit tests viết và pass (coverage > 80%)
□ Integration tests pass
□ Acceptance Criteria met và verified
□ Product Owner approval
□ Documentation updated
□ No critical bugs
□ Deployed to staging environment
```

### 8.3 Sprint Ceremonies

| Ceremony | Frequency | Duration | Participants |
|----------|-----------|----------|--------------|
| Sprint Planning | Start of Sprint | 2 hours | All team |
| Daily Standup | Daily | 15 mins | Dev team |
| Sprint Review | End of Sprint | 1 hour | All + Stakeholders |
| Sprint Retrospective | End of Sprint | 1 hour | All team |

---

## PHỤ LỤC

### A. Tham chiếu User Stories theo Sprint

| Sprint | User Stories | Total SP |
|--------|--------------|----------|
| Sprint 1 | US01, US02 | 8 SP |
| Sprint 2 | US04, US05, US07 | 16 SP |
| Sprint 3 | US03, US06, US08, US14 | 15 SP |
| Sprint 4 | US09, US10, US11 | 13 SP |
| Sprint 5 | US12, US13 | 8 SP |
| **Total** | **14 US** | **60 SP** |

### B. Key Milestones

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| M1 - Project Kickoff | 01/03/2026 | Environment ready |
| M2 - Auth Complete | 07/03/2026 | Login/Signup working |
| M3 - Book Module Done | 14/03/2026 | Full book CRUD |
| M4 - Search Complete | 21/03/2026 | Search & Filter working |
| M5 - Purchase Flow Done | 28/03/2026 | Transaction complete |
| M6 - Rating Complete | 04/04/2026 | All features done |
| M7 - UAT Complete | 10/04/2026 | UAT passed |
| M8 - Demo Ready | 12/04/2026 | Final presentation |

### C. Contact Information

| Vai trò | Người phụ trách | Email |
|---------|-----------------|-------|
| Product Owner | [Tên] | [Email] |
| Scrum Master | [Tên] | [Email] |
| Tech Lead | [Tên] | [Email] |

---

*Tài liệu này được tạo theo chuẩn Agile/Scrum Project Management*  
*Cập nhật lần cuối: 22/02/2026*  
*Phiên bản: 1.0*