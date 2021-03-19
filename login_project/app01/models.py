from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=32)  # 会在数据库中创建一个varchar类型的字段最大长度32
    pass_word = models.CharField(max_length=32)  # varchar(32)
