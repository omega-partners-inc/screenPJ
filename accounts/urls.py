from django.contrib import admin
from django.urls import path
#from .views import checkview,completeview,
from .views import user_data_confirm,user_data_create,user_data_input,loginview,userhomeview
from . import views

app_name='accounts'

urlpatterns = [
    #path('', views.Top.as_view(), name='userhome'),
    #path('admin/', admin.site.urls),
    path('user_data_input/',user_data_input, name='user_data_input'),    
    #path('check/', checkview,name='check'),
    #path('register/', registerview,name='register'),
    #path('complete/', completeview,name='complete'), 
    path('user_data_confirm/', user_data_confirm, name='user_data_confirm'),   
    path('user_data_create/', user_data_create, name='user_data_create'),
    #path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', loginview, name='login'),
    #path('logout/',logoutview, name='logout'),
    path('userhome/',userhomeview,name='userhome'),
    path('logout/', views.Logout.as_view(), name='logout'),
]