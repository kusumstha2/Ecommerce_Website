from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Category(models.Model):
    name=models.CharField(max_length=225)
    
    def __str__(self) -> str:
        return self.name 

class Recipe(models.Model):
    name=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    ingredient= models.TextField()
    instruction=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True)
    image=models.ImageField()
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.name