from django.shortcuts import render
# from Car.models import Vechile

# Create your views here.

def book_car(request,id):
	get_by_id=Vechile.objects.filter(id=id)
	return render(request,'booking.html',{'data':get_by_id})