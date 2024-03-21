from django.urls import path
from Car.views import list_categories,car_lists,index

app_name='Car'

urlpatterns=[
path('list categories',list_categories,name='categories'),
path('car-lists',car_lists,name='car_lists'),
path('',index,name='index')

	]