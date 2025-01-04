from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length=200, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gamecrit_post_blog"
    )
    post_field = models.TextField()
    youtube_link = models.URLField(max_length=300, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_private = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.post_name} | written by {self.username}"

class Comment(models.Model):
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    comment_field = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment{self.comment_field} by {self.username}"