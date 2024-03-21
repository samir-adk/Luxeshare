from django.shortcuts import render

# Create your views here.

def book_car(request,id):
	return render(request,'booking.html')