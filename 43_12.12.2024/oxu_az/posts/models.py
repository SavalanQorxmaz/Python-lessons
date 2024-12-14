from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Writer(models.Model):
    name = models.CharField(max_length=64)
    user = models.OneToOneField(User, default='Anonim', on_delete=models.SET_DEFAULT)

class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=6000)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)