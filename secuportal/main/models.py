from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    post_number = models.IntegerField(default=0)  # 게시물 번호 필드 추가

    def save(self, *args, **kwargs):
        if not self.id:  # 새로운 게시물일 경우에만 번호 할당
            last_post = Post.objects.order_by('-post_number').first()
            self.post_number = (last_post.post_number + 1) if last_post else 1
        super().save(*args, **kwargs)
