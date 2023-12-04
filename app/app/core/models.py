from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        
        return user
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using.self_db)
        return user

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True),
    name = models.CharField(max_length=30),
    is_active = models.BooleanField(default=True),
    is_staff = models.BooleanField(default=False),
    
    objects= UserManager()
    
    USERNAME_FIELD = 'email'