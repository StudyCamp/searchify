from django.contrib import admin
from .models import User, Post, Tag

# Admin interface
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    readonly_fields = ('id',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'poster', 'timestamp', 'image')
    readonly_fields = ('id',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)