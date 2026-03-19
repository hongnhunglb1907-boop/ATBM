"""
Models for Ratings App
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from books.models import Book


class Rating(models.Model):
    """Đánh giá người bán"""

    RATING_CHOICES = [(i, f'{i} sao') for i in range(1, 6)]  # 1-5 sao

    # Người đánh giá và người bị đánh giá
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_ratings',
        verbose_name='Người bán (được đánh giá)'
    )
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='given_ratings',
        verbose_name='Người đánh giá'
    )

    # Sách liên quan
    book = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ratings',
        verbose_name='Sách đã mua'
    )

    # Đánh giá
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Số sao'
    )
    comment = models.TextField(
        blank=True,
        max_length=500,
        verbose_name='Bình luận'
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày đánh giá')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Đánh giá'
        verbose_name_plural = 'Danh sách đánh giá'
        ordering = ['-created_at']
        # Một người chỉ đánh giá một seller một lần cho mỗi book
        unique_together = ['seller', 'reviewer', 'book']

    def __str__(self):
        return f"{self.reviewer.username} đánh giá {self.seller.username}: {self.rating}★"

    @property
    def star_display(self):
        """Hiển thị số sao dạng HTML"""
        stars = ''
        for i in range(1, 6):
            if i <= self.rating:
                stars += '★'
            else:
                stars += '☆'
        return stars

    def save(self, *args, **kwargs):
        """Override save để cập nhật reputation của seller"""
        super().save(*args, **kwargs)
        # Cập nhật điểm uy tín của người bán
        if self.seller and hasattr(self.seller, 'profile'):
            self.seller.profile.update_reputation()
