from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

"""
    The default user model in Django uses the username to login, but here
    we want to modify the process so the user will use the email to login.
    Secondly,since we are changing how users are created (requiring an email
     instead of a username), we need a custom manager to handle that logic,
     and that's why we create a Manager class.

"""


class UserProfileManager(BaseUserManager):
    """"Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """"Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """"Create and save a new superuser with the given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"DB model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # in the beginning, all the users are activated
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()  # to know how to this customised model works with the CLI
    USERNAME_FIELD = 'email'  # when user tries to login, use the email as ain ID, not the username
    REQUIRED_FIELDS = ['name']  # when creating a superuser, ask also for the name not only the email

    # Functions to interact with the base model
    def get_full_name(self):
        """Retieve the full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrieve the short name of the user"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email
