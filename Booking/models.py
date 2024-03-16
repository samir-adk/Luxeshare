from django.db import models
from Users.models import User,BaseModel
from Car.models import Vehicle
# Create your models here.


class Booking(BaseModel):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='bookings', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        duration_hours = (self.end_time - self.start_time).total_seconds() / 3600
        self.total_cost = duration_hours * self.vehicle.hourly_rate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking: {self.vehicle} by {self.user.username}"


