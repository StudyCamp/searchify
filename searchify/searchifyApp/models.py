from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=64)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False, default="No Images", upload_to="images/")

class Tag(models.Model):
    tag = models.CharField(max_length=32, default=None)
    tag_post = models.ManyToManyField(Post, related_name="tagged_posts")

