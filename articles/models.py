from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    thumbnail = models.ImageField(blank=True, upload_to='images/%y/%m/%d/thumbnails', null=True)
    image = models.ImageField(blank=True, upload_to='images/%y/%m/%d/', null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
