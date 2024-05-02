from django.shortcuts import render
from Car.models import Vehicle
# Create your views here.

def list_categories(request):
	pass

def car_lists(request):
	get_data=Vehicle.objects.all()
	return render(request,'car_list.html',{'data':get_data})

def index(request):
	featured_cars=Vehicle.objects.all().filter(featured=True)
	new_cars=Vehicle.objects.all().filter(newest_car=True)
	return render(request,'index.html',{'featured_cars':featured_cars,'new_cars':new_cars})