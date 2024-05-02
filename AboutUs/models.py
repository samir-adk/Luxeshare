from django.db import models
from Users.models import BaseModel
# Create your models here.

class ContactUs(BaseModel):
	email=models.CharField(max_length=40)
	phone=models.CharField(max_length=40)
	message=models.CharField(max_length=200)

	def __str__(self):
		return f"{self.email}:{self.message}"