from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here

class BaseModel(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True



class User(AbstractUser):
	phone_number=models.IntegerField(null=True,blank=True)









