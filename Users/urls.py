from django.urls import path
from Users.views import signup,loginz,logout_view
# CustomPasswordResetView
from django.contrib.auth import views as auth_views

app_name='Users'

urlpatterns=[
path('signup',signup,name='signup'),
path('login',loginz,name='login'),
path('logout/', logout_view, name='logout'),

	]