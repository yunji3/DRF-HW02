from django.db import models
from user.models import User
# Create your models here.


class Category(models.Model):
    # ForeignKey - 다른 데이터베이스를 가져와서 사용하겠다.
    name = models.CharField(max_length=100)
    dec = models.TextField(max_length=256)

    def __str__(self):
        return self.name


class Article(models.Model):
    # ForeignKey - 다른 데이터베이스를 가져와서 사용하겠다.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."
