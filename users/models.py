from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    CHOICES = (('M','Male'),('F','Female'))

    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=CHOICES,default='M')
    avartar = models.ImageField(upload_to='uploads')

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            profile = Profile(user=instance)
            profile.save()


