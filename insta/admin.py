from django.contrib import admin
from .models import Post,UserFollowing,Like
# Register your models here.
admin.site.register(Post)
admin.site.register(UserFollowing)
admin.site.register(Like)