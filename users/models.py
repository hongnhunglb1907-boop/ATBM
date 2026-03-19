"""
Models for Users App
"""
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Hồ sơ mở rộng của User"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    # Thông tin sinh viên
    student_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name='Mã số sinh viên'
    )

    # Thông tin liên hệ (BẮT BUỘC)
    phone_number = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        verbose_name='Số điện thoại'
    )

    # Link liên hệ (BẮT BUỘC)
    facebook_link = models.URLField(
        blank=False,
        null=False,
        verbose_name='Link Facebook'
    )
    zalo_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='Link Zalo'
    )

    # Thông tin cá nhân
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='Ảnh đại diện'
    )
    bio = models.TextField(
        blank=True,
        max_length=500,
        verbose_name='Giới thiệu bản thân'
    )

    # Địa chỉ
    address = models.CharField(
        max_length=300,
        blank=True,
        verbose_name='Địa chỉ gặp giao dịch'
    )

    # Thống kê
    reputation_score = models.FloatField(
        default=0.0,
        verbose_name='Điểm uy tín'
    )
    total_reviews = models.PositiveIntegerField(
        default=0,
        verbose_name='Số lượt đánh giá'
    )

    # Metadata
    is_verified = models.BooleanField(
        default=False,
        verbose_name='Đã xác minh'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hồ sơ người dùng'
        verbose_name_plural = 'Hồ sơ người dùng'

    def __str__(self):
        return f"Profile: {self.user.get_full_name() or self.user.username}"

    @property
    def average_rating(self):
        """Điểm đánh giá trung bình"""
        from ratings.models import Rating
        ratings = Rating.objects.filter(seller=self.user)
        if ratings.exists():
            return sum(r.rating for r in ratings) / ratings.count()
        return 0.0

    def update_reputation(self):
        """Cập nhật điểm uy tín"""
        from ratings.models import Rating
        ratings = Rating.objects.filter(seller=self.user)
        self.total_reviews = ratings.count()
        if self.total_reviews > 0:
            self.reputation_score = sum(r.rating for r in ratings) / self.total_reviews
        else:
            self.reputation_score = 0.0
        self.save()

    @property
    def display_name(self):
        """Tên hiển thị"""
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    @property
    def total_books_sold(self):
        """Tổng số sách đã bán"""
        return self.user.books_for_sale.filter(status='sold').count()

    @property
    def total_books_listed(self):
        """Tổng số bài đăng"""
        return self.user.books_for_sale.count()


# Signal để tự động tạo UserProfile khi tạo User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Tự động tạo UserProfile khi tạo User mới.
    Lưu ý: UserProfile hiện có các field bắt buộc (phone, facebook, zalo)
    nên signal này chỉ tạo profile rỗng. Form đăng ký sẽ chịu trách nhiệm
    điền đầy đủ thông tin bắt buộc.
    """
    if created:
        # Tạo profile với các giá trị tạm nhiên (sẽ được update bởi form đăng ký)
        UserProfile.objects.create(
            user=instance,
            phone_number='',
            facebook_link='',
            zalo_link=''
        )
