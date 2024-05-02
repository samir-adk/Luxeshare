from django.shortcuts import render,redirect
from Users.forms import UserForm,LoginForm
# CustomPasswordResetForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from Users.models import CustomUser
from django.contrib.auth.hashers import make_password
# Create your views here.



def signup(request):
    form=UserForm()
    if request.method=='POST':
        form_data=UserForm(request.POST)
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        hashed_password=make_password(confirm_password)

        if email and phone_number and password and confirm_password:
            save_data=CustomUser.objects.create(email=email,phone_number=phone_number,password=hashed_password,username=email)
            save_data.save()
            return render(request, 'login.html', {'form': form})

        else:
            return render(request,'signup.html')
    return render(request,'signup.html')


def loginz(request):
    form = LoginForm()
    if request.method == 'POST':
        email=request.POST.get('username')
        password=request.POST.get('password')
        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('Car:index')
            else:
                    # Both email and phone number authentication failed
                    return render(request, 'login.html', {'form': form})
        else:
            # Form validation failed
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {'form': form})




# class CustomPasswordResetView(PasswordResetView):
#     form_class = CustomPasswordResetForm
#     