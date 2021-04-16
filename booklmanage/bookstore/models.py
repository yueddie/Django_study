from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=12)


class Book(models.Model):
    name = models.CharField(max_length=32)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)
    """
        on_delete其他参数
        on_delete=None, # 删除关联表中的数据时,当前表与其关联的field的行为
        on_delete=models.CASCADE, # 删除关联数据,与之关联也删除
        on_delete=models.DO_NOTHING, # 删除关联数据,什么也不做
        on_delete=models.PROTECT, # 删除关联数据,引发错误ProtectedError
        models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
        on_delete=models.SET_NULL, # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
        models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
        on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
        on_delete=models.SET, # 删除关联数据,
    """


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')
