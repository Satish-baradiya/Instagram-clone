from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField()
    description = models.CharField(max_length=250)
    likes = models.PositiveIntegerField(default=0)
    comments = models.CharField(max_length=100,null=True)
    user_likes = models.ManyToManyField(User,related_name='user_likes')

    def __str__(self) -> str:
        return self.user.username



class UserFollowing(models.Model):
    user_id = models.OneToOneField(User, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ManyToManyField(User, related_name="followers",blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_id.username



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    alreadyLiked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user} like {self.post}"


@receiver(post_save, sender=User)
def create_user_following(sender, instance, created, **kwargs):
    if created:
        UserFollowing.objects.create(user_id = instance)