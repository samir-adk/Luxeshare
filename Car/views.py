from django.shortcuts import render
from Car.models import Vehicle
# Create your views here.

def list_categories(request):
	pass

def car_lists(request):
	get_data=Vehicle.objects.all()
	return render(request,'car_list.html',{'data':get_data})

def index(request):
	return render(request,'index.html')