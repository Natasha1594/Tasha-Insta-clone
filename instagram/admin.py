from django.contrib import admin
from .models import Photo, Profile, Post, Comment, Follow, Upload

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Photo)
admin.site.register(Upload)

