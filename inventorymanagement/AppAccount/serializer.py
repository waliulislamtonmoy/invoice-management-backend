
# from django.contrib.auth import get_user_model
# User =get_user_model

from AppAccount.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User 
        fields=['firstName','lastName','email','password','mobile']
    #method=1  
    # def create(self,validated_data):
    #     user=User(
    #         email=validated_data['email']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    
    #method=2
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        user.save()
        return user    
    
      
        

