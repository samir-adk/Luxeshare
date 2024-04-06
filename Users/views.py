from django.shortcuts import render,redirect
from Users.forms import UserForm,LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def signup(request):
    form=UserForm()
    if request.method=='POST':
        form_data=UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('Users:login')
        else:
            return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})


def loginz(request):
    form = LoginForm()
    if request.method == 'POST':
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            email = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('Car:index')
            else:
                # If authentication fails using email, try phone number
                user = authenticate(request, phone_number=email, password=password)
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




