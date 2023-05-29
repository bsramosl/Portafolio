from django.urls import path
from PrincipalApp import views 
from django.contrib.auth.decorators import login_required  
from .forms import * 



app_name = 'Long'
urlpatterns = [       
    path('',views.Index.as_view(),name='Inicio'), 
    path('About/',views.About.as_view(),name='About'),   
    path('Contact/',views.Contact,name='Contact'),   
    ]