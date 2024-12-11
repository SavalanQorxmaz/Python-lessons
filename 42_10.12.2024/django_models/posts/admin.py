from django.contrib import admin
from .models import Writer, Post
# Register your models here.


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)