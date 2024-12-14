from django.contrib import admin

# Register your models here.

from .models import Writer, Post

admin.site.register(Writer)

admin.site.register(Post)