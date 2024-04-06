from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class User(AbstractUser):
    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['phone_number']  # Make phone number a required field

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    # Add any other custom fields or methods as needed
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email




