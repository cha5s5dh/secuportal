from django.db import models

class Post(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    content = models.TextField(default='')

    def __str__(self):
        return self.title
