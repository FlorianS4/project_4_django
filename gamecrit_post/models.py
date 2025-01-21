from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, default="", null=False)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gamecrit_post_blog"
    )
    post_field = models.TextField()
    youtube_link = models.URLField(max_length=300, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    gamecrit_post_blog_likes = models.ManyToManyField(User, related_name="gamecrit_post_like", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmark", default=None, blank=True)
    post_image = CloudinaryField('image,', default='placeholder')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.post_name} | written by {self.username}"

    def number_of_gamecrit_post_blog_likes(self):
        return self.gamecrit_post_blog_likes.count()

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