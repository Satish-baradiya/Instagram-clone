from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField()
    description = models.CharField(max_length=250)
    likes = models.PositiveIntegerField(default=0)
    comments = models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.user.username



class UserFollowing(models.Model):
    user_id = models.OneToOneField(User, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ManyToManyField(User, related_name="followers",blank=True)
    created = models.DateTimeField(auto_now_add=True)