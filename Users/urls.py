from django.urls import path
from Users.views import signup,loginz

app_name='Users'

urlpatterns=[
path('signup',signup,name='signup'),
path('login',loginz,name='login'),

	]