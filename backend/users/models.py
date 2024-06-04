from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UsersManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError('Email is required')
        
        user = self.model(email=self.normalize_email(email), full_name=full_name)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            full_name = full_name,
            password = password
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class Users(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    full_name = models.CharField(max_length=255, default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    objects = UsersManager()

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True