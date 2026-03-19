"""
Forms for Ratings App
"""
from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    """Form đánh giá người bán"""

    class Meta:
        model = Rating
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Chia sẻ trải nghiệm của bạn về người bán...'
            }),
        }
        labels = {
            'rating': 'Số sao đánh giá',
            'comment': 'Bình luận',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tùy chỉnh choices cho rating
        self.fields['rating'].choices = [
            (5, '⭐⭐⭐⭐⭐ - Xuất sắc (5 sao)'),
            (4, '⭐⭐⭐⭐ - Tốt (4 sao)'),
            (3, '⭐⭐⭐ - Khá (3 sao)'),
            (2, '⭐⭐ - Trung bình (2 sao)'),
            (1, '⭐ - Kém (1 sao)'),
        ]
