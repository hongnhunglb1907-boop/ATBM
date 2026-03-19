"""
Forms for Books App
"""
from django import forms
from .models import Book, Subject


class BookForm(forms.ModelForm):
    """
    Form đăng/cập nhật sách
    Lưu ý: Thông tin liên hệ đã được loại bỏ - hệ thống sẽ tự động
    hiển thị thông tin từ UserProfile của người bán
    """

    class Meta:
        model = Book
        fields = [
            'title', 'author', 'subject', 'price', 'original_price',
            'condition', 'description', 'notes', 'cover_image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên sách'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tên tác giả (nếu có)'
            }),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'VD: 150000'
            }),
            'original_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'VD: 200000 (để trống nếu không có)'
            }),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Mô tả về sách...'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Ghi chú thêm (gạch bớt, v.v.)'
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'title': 'Tên sách',
            'author': 'Tác giả',
            'subject': 'Môn học',
            'price': 'Giá bán (VNĐ)',
            'original_price': 'Giá bìa (VNĐ)',
            'condition': 'Tình trạng',
            'description': 'Mô tả chi tiết',
            'notes': 'Ghi chú',
            'cover_image': 'Ảnh bìa',
        }


class BookSearchForm(forms.Form):
    """Form tìm kiếm sách"""
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tìm kiếm theo tên sách, tác giả...'
        })
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=False,
        empty_label='-- Tất cả môn học --',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    condition = forms.ChoiceField(
        choices=[('', '-- Tất cả tình trạng --')] + Book.CONDITION_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    min_price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Giá tối thiểu'
        })
    )
    max_price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Giá tối đa'
        })
    )
    sort = forms.ChoiceField(
        choices=[
            ('-created_at', 'Mới nhất'),
            ('created_at', 'Cũ nhất'),
            ('price', 'Giá thấp đến cao'),
            ('-price', 'Giá cao đến thấp'),
            ('-view_count', 'Nhiều lượt xem'),
        ],
        required=False,
        initial='-created_at',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
