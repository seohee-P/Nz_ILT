from django.contrib import admin
from .models import Department

# Register your models here.

admin.site.register(Department)



# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'photo_tag', 'title', 'is_public', 'created_at', 'updated_at']
#     list_display_links = ['title']
#     list_filter = ['created_at', 'is_public']
#     search_fields = ['title']

#     def photo_tag(self, post):
#         if post.photo:
#             return mark_safe(f'<img src="{post.photo.url}" style="width: 72px" />')
