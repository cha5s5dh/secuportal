from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, default='일반')
    content = RichTextField()
    original_time = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    author = models.CharField(max_length=50, default='임시 작성자')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
