from django.contrib import admin
from test_app.models import Book, Post, UserProfile

admin.site.register(Book)
admin.site.register(Post)
admin.site.register(UserProfile)
