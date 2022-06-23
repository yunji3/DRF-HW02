from datetime import timedelta
from email import contentmanager
from itertools import product
from logging.handlers import RotatingFileHandler
from django.db import models
from user.models import User as UserModel


class Product(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    show_start_at = models.DateTimeField(default="2022-06-20 00:00:00")
    show_end_at = models.DateTimeField(default="2022-06-25 00:00:00")
    thumbnail = models.ImageField(upload_to='product/img', height_field=None, width_field=None, max_length=100)

    is_active = models.BooleanField('활성화 여부', default=True)

    def __str__(self):
        return f'Product : {self.title} - {self.author}'

class Review(models.Model):
    author = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    content = models.TextField('내용', default="")
    rating = models.IntegerField('평점', default=0)
    created_at = models.DateTimeField('작성일', auto_now_add=True)

    def __str__(self):
        return f'Review : {self.product.title} - {self.author.username} ({self.rating})'