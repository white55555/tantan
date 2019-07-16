from django.db import models

class User(models.Model):
    SEXS = (
        (1,'男'),
        (2,'女'),
        (0,'未知')
    )
    LOCATIONS = (
        ('gz','广州'),
        ('bj','北京'),
        ('sz','深圳'),
        ('hz','杭州')
    )

    #id = models.CharField(max_length=20,unique=True)
    phonenum = models.CharField(max_length=20,unique=True)
    birth_year = models.IntegerField(default=2000)
    nickname = models.CharField(max_length=20)
    sex = models.IntegerField(choices=SEXS,default=0)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=16,choices=LOCATIONS,default='gz')
    class Meta:
        db_table = 'users'




