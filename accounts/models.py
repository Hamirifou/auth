from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    description=models.TextField(blank=True,null=True)
    first_name = models.CharField(max_length=255,null=True,blank=True,)
    last_name = models.CharField(max_length=255,null=True,blank=True,)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_creator=models.BooleanField(default=False)
    REQUIRED_FIELDS = ['location','first_name','last_name']
    def __str__(self):
        return self.user.username
    