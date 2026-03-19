"""
Admin for Books App
"""
from django.contrib import admin
from .models import Book, Subject, BookImage


class BookImageInline(admin.TabularInline):
    """Inline admin cho book images"""
    model = BookImage
    extra = 1
    fields = ['image', 'order']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin interface cho Book"""
    list_display = ['title', 'seller', 'subject', 'price', 'status', 'condition', 'view_count', 'created_at']
    list_filter = ['status', 'condition', 'subject', 'created_at']
    search_fields = ['title', 'author', 'description', 'seller__username']
    readonly_fields = ['view_count', 'created_at', 'updated_at']
    inlines = [BookImageInline]
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'author', 'subject')
        }),
        ('Thông tin bán hàng', {
            'fields': ('price', 'original_price', 'condition', 'status')
        }),
        ('Mô tả', {
            'fields': ('description', 'notes')
        }),
        ('Hình ảnh', {
            'fields': ('cover_image',)
        }),
        ('Thông tin liên hệ', {
            'fields': ('contact_phone', 'contact_facebook', 'contact_zalo')
        }),
        ('Thông tin khác', {
            'fields': ('seller', 'view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Admin interface cho Subject"""
    list_display = ['code', 'name', 'created_at']
    search_fields = ['name', 'code']
    list_per_page = 50


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    """Admin interface cho BookImage"""
    list_display = ['book', 'order', 'created_at']
    list_filter = ['created_at']
