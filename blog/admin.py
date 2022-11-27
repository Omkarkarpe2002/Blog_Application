from django.contrib import admin
from blog.models import Post, BlogComment, CoepPost

admin.site.register((BlogComment))
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js')
@admin.register(CoepPost)
class CoepPostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js')