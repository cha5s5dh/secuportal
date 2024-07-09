from django.db import models

class Post(models.Model):
    CATEGORIES = (
        ('temp1', '보안뉴스'),
        ('temp2', '보안가이드'),
        ('temp3', '임시3'),
        ('temp4', '임시4'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    original_time = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def get_category_display(self):
        return dict(Post.CATEGORIES).get(self.category, 'Unknown')
