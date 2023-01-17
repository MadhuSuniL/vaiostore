from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    typeofuser = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    profile = models.ImageField()
    
choice = (
        ("Sarees","Sarees"),
        ("Dresses","Dresses"),
        ("Baby Costumes","Baby Costumes"),
        ("Girls Costumes","Girls Costumes"),
    )
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    img1 = models.ImageField()    
    img2 = models.ImageField()    
    img3 = models.ImageField()    
    img4 = models.ImageField()    
    img5 = models.ImageField()
    yt_link = models.URLField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    prize = models.IntegerField(default=10000)
    description = models.TextField()
    catry = models.CharField(max_length=20,choices=choice,default=choice[0])
    
    
    
    
        
