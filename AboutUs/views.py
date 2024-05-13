from django.shortcuts import render
from AboutUs.models import ContactUs
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

def contact_us(request):
	if request.method=='POST':
		email=request.POST.get('email')
		message=request.POST.get('message')
		create_data=ContactUs.objects.create(email=email,message=message)
		create_data.save()
	return redirect(reverse('Car:index'))



