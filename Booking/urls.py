from django.urls import path
from Booking.views import book_car,confirm_booking

app_name='Booking'

urlpatterns=[
path('book-car/<int:id>',book_car,name='book_car'),
path('confirm-booking',confirm_booking,name='confirm_booking'),
]