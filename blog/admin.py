# https://testdriven.io/blog/django-custom-user-model/

from .models import Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Main list
    list_display = (
        'short_title',
        'author_display_name',
        'date_published',
        'date_edited',
    )
    list_display_links = ('short_title', )
    list_filter = ('author__email', )
    search_fields = (
        'title',
        'author__first_name',
        'author__last_name',
        'author__email',
        'content',
    )

    # Specific Post instance
    fieldsets = (
        ('Meta', {'fields': (
            'author',
            'date_published',
            'date_edited',
        )}),
        ('Details', {'fields': (
            'title',
            'content',
        )}),
    )
    readonly_fields = ['date_published', 'date_edited', ]

    # Additional or renamed attributes
    def author_display_name(self, obj):
        return obj.author.display_name
