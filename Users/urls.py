from django.urls import path
from Users.views import signup,loginz
# CustomPasswordResetView
from django.contrib.auth import views as auth_views

app_name='Users'

urlpatterns=[
path('signup',signup,name='signup'),
path('login',loginz,name='login'),
# path('password_reset/',CustomPasswordResetView.as_view(), name='password_reset'),

#     path('password_reset/done/', 
#          auth_views.PasswordResetDoneView.as_view(
#              template_name='password_reset_done.html'
#          ), 
#          name='password_reset_done'),

#     path('reset/<uidb64>/<token>/', 
#          auth_views.PasswordResetConfirmView.as_view(
#              template_name='password_reset_confirm.html'
#          ), 
#          name='password_reset_confirm'),

#     path('reset/done/', 
#          auth_views.PasswordResetCompleteView.as_view(
#              template_name='password_reset_complete.html'
#          ), 
#          name='password_reset_complete'),

	]