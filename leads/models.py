from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lead(models.Model):
    
    first_name =models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age =models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
        
    def __str__(self):
        return self.user.username
    





# Version 2

# from django.db import models 
# from django.contrib.auth import get_user_model

# User = get_user_model()     

# class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     ('Youtube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )
    
    # first_name =models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    # age =models.IntegerField(default=0)
    # agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)