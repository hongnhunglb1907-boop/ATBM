"""
Admin for Ratings App
"""
from django.contrib import admin
from .models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Admin interface cho Rating"""
    list_display = ['seller', 'reviewer', 'book', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = [
        'seller__username',
        'reviewer__username',
        'comment',
        'book__title'
    ]
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'seller', 'reviewer', 'book'
        )
