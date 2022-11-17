from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField()
    description = models.CharField(max_length=250)
    likes = models.PositiveIntegerField(default=0)
    comments = models.CharField(max_length=100,null=True)
