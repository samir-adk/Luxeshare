from django.shortcuts import render
from Car.models import Vehicle
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from Booking.models import BookingCar
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def book_car(request,id):
    get_by_id=Vehicle.objects.filter(id=id)
    return render(request,'booking.html',{'data':get_by_id})

@csrf_exempt
@login_required
def confirm_booking(request):
    if request.method=="POST":
        data=json.loads(request.body)
        start_timestamp = data.get('start')
        end_timestamp = data.get('end')
        total_cost = data.get('total_cost')
        owner_name=data.get('owner_name')
        logged_user=data.get('logged_user')
        vechile_id=data.get('vechile_id')
        hourly_rate=data.get('hourly_rate')
        already_booked=BookingCar.objects.filter(vehicle_id=vechile_id).filter(start_time__gte=start_timestamp,end_time__lte=end_timestamp,cancelled=False)
        if already_booked.exists():
            return JsonResponse({'success': False})
        else:
            save_data=BookingCar.objects.create(hourly_rate=hourly_rate,user_id=request.user.id,vehicle_id=vechile_id,start_time=start_timestamp,end_time=end_timestamp,total_cost=total_cost,booked=True)
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': True})

@login_required
def view_booking(request):
    my_booking=BookingCar.objects.filter(user__email=request.user.email,cancelled=False)
    return render(request,'booking_cart.html',{'data':my_booking})
@login_required
def remove_booking(request,id):
    update_id=BookingCar.objects.filter(id=id).update(cancelled=True)
    return redirect(reverse('Booking:view_booking'))

