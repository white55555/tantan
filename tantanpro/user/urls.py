from django.urls import path
from user.views import *
app_name='user'


urlpatterns=[
    path('login/',login,name='login'),
    path('get_avater/',get_avater,name='get_avater'),
    path('get_profile/',get_profile,name='get_profile'),
    path('set_profile/',set_profile,name='set_profile'),
    path('verify_phone/',verify_phone,name='verify_phone'),

]