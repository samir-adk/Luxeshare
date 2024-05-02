from django.shortcuts import render
from AboutUs.models import ContactUs
from django.http import JsonResponse
# Create your views here.

def contact_us:
	if request.method=='POST':
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		message=request.POST.get('message')
		create_data=ContactUs.objects.create(email=email,phone=phone,message=message)
		create_data.save()
		return JsonResponse({'message':'created data'})



