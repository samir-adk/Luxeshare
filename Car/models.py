from django.db import models
from Users.models import CustomUser,BaseModel
# Create your models here.

class CarCategory(BaseModel):
    car_category_name=models.TextField(max_length=25)
    Note=models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.car_category_name

class CarCompany(BaseModel):
    car_company_category=models.ForeignKey(CarCategory,on_delete=models.CASCADE)
    car_company_name=models.TextField(max_length=100)

    def __str__(self):
        return f'{self.car_company_category}:{self.car_company_name}'




class Owner(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Vehicle(BaseModel):
    MANUAL = 'manual'
    AUTOMATIC = 'automatic'
    
    TRANSMISSION_CHOICES = [
        (MANUAL, 'Manual'),
        (AUTOMATIC, 'Automatic'),
    ]
    owner = models.ForeignKey(Owner, related_name='vehicles', on_delete=models.CASCADE)
    vechile_category=models.ForeignKey(CarCompany,related_name='vechile_category',on_delete=models.CASCADE,null=True,blank=True)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=50, unique=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    featured=models.BooleanField(default=False)
    newest_car=models.BooleanField(default=False)
    image = models.ImageField(upload_to='vehicle_images/',null=True,blank=True)
    about=models.CharField(max_length=200)
    transmission=models.CharField(max_length=20,choices=TRANSMISSION_CHOICES,default=AUTOMATIC)

    def __str__(self):
        return f"{self.model} ({self.year})"









