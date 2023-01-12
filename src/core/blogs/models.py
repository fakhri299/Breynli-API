from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    body = RichTextField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="blogs")
    image = models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")

    def __str__(self) -> str:
        return self.title
