from django.db import models
from Users.models import User,BaseModel
from Car.models import Vehicle
from datetime import datetime
# Create your models here.


class BookingCar(BaseModel):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='bookings', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    booked=models.BooleanField(default=False)
    cancelled=models.BooleanField(default=False)
    hourly_rate=models.DecimalField(max_digits=10,default=0,decimal_places=2)


    def save(self, *args, **kwargs):
        self.start_time = datetime.strptime(self.start_time, '%Y-%m-%d %H:%M:%S')
        self.end_time = datetime.strptime(self.end_time, '%Y-%m-%d %H:%M:%S')
        duration_hours = (self.end_time - self.start_time).total_seconds() / 3600
      
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking: {self.vehicle} by {self.user.username}"


