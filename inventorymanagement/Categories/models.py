from django.db import models
from AppAccount.models import User
# Create your models here.
# from django.contrib.auth import get_user_model
# User=get_user_model()

class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.RESTRICT)
    name=models.CharField( max_length=100)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now=True )
    
    def __str__(self):
        return self.name