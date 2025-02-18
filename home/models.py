from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    platform = models.CharField()
    release_date = models.CharField()
    genre = models.CharField()
    publisher = models.CharField()
    developer = models.CharField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="game_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)