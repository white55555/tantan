from django.urls import path
from user.views import *
app_name='user'


urlpatterns=[
    path('login/',login,name='login'),
    path('verify_phone/',verify_phone,name='verify_phone'),
    
]