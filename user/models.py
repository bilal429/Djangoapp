from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    USER_ROLES = (
        ('shop', 'Shop'),
        ('customer', 'Customer'),
    )

    user_role = models.CharField(max_length=10, choices=USER_ROLES, default='customer')
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    shop_address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
                    