from django.contrib import admin
from django.urls import path
from .views import user_data_confirm,user_data_create,user_data_input,loginview,userhomeview
from . import views

app_name='accounts'

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('user_data_input/',user_data_input, name='user_data_input'),    
    path('user_data_confirm/', user_data_confirm, name='user_data_confirm'),   
    path('user_data_create/', user_data_create, name='user_data_create'),
    path('login/', loginview, name='login'),
    path('userhome/',userhomeview,name='userhome'),
    path('logout/', views.Logout.as_view(), name='logout'),
]