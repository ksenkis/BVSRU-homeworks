from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
