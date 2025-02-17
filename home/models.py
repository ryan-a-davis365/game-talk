from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    platform = models.TextField()
    release_date = models.TextField()
    genre = models.TextField()
    publisher = models.CharField()
    developer = models.CharField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="game_posts"
    )