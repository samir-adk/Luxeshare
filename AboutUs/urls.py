from django.urls import path
from .views import contact_us

app_name='AboutUs'
urlpatterns=[(
path('contact_us',contact_us,name='contact_us')
	)]