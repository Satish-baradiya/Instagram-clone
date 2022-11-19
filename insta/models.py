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

    def __str__(self) -> str:
        return self.user.username



class UserFollowing(models.Model):
    user_id = models.OneToOneField(User, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ManyToManyField(User, related_name="followers",blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_id.username


# @receiver(pre_save, sender=User)
# def correct_price(sender,**kwargs):
#     user= kwargs['instance']
#     newfollow = UserFollowing.objects.create(user_id=user)
#     newfollow.save()
    # price_of_product = Product.objects.get(id=cart_items.product.id)
    # cart_items.price = cart_items.quantity * float(price_of_product.price)