from django.db import models


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = models.TextField()
    comments = models.TextField()
