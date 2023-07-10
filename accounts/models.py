from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    # USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    class Meta:
        pass
        
    def __str__(self):
            return self.username

