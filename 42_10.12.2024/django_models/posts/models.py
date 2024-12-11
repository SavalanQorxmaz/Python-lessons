from django.db import models

# Create your models here.

class Writer(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=64, null=False, default='Title' )
    description = models.TextField(max_length=6000, null=False, default='Description')
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, default=None)
    
    def __str__(self) -> str:
        return f'{self.writer} {self.title}'
