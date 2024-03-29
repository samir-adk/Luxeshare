from django.urls import path
from Booking.views import book_car,confirm_booking,view_booking,remove_booking

app_name='Booking'

urlpatterns=[
path('book-car/<int:id>',book_car,name='book_car'),
path('confirm-booking',confirm_booking,name='confirm_booking'),
path('view-booking',view_booking,name='view_booking'),
path('remove-booking/<int:id>',remove_booking,name='remove_booking'),
]