from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    platform = models.CharField(max_length=100, default='Unknown')
    release_date = models.CharField(max_length=100, default='Unknown')
    genre = models.CharField(max_length=100, default='Unknown')
    status = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100, default='Unknown')
    developer = models.CharField(max_length=100, default='Unknown')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_posts')
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.created_by}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.created_by}"