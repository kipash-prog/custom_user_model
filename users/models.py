from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("you must have email address")
        email=self.normalize_email(email)
        user=self.model(
            email,
            username=username,   
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
        
    def create_superuser(self,email,username,passsword=None):
        user=self.create_user(
            email,
            username=username,
            password=passsword
        )
        user.is_admin=True
        user.save(using=self._db)
        
        return user
    
    
class users(AbstractBaseUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=12)
    is_admin=models.BooleanField(default=True)
    
    
    objects=CustomUserManager()
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","password"]
    
    