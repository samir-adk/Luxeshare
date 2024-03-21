from django.urls import path
from Booking.views import book_car

app_name='Booking'

urlpatterns=[
path('book-car/<int:id>',book_car,name='book_car')
]