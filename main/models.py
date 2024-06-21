# main/models.py

from django.db import models

class Post(models.Model):
    number = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
