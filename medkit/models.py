from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Information(models.Model):
    medicine_name = models.CharField(max_length=30)
    expiry_date = models.DateField(
        error_messages={'invalid': 'Please enter in "YYYY-MM-DD" Format!'})
    quantity = models.IntegerField(
        error_messages={'invalid': 'Please enter numbers!'})
    marked_price = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    discount = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    company = models.CharField(max_length=30)
    dealer = models.CharField(max_length=30)


class Sale_Information(models.Model):
    medicine_name = models.CharField(max_length=30)
    quantity = models.IntegerField(
        error_messages={'invalid': 'Please enter numbers!'})
    marked_price = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    discount = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    sale_id = models.ForeignKey(Information, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.content