from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import User_data
from .forms import User_data_Form

# Create your views here.

def registerview(request):
    if request.method == 'POST':
        obj = User_data()
        user_data = User_data_Form(request.POST,instance=obj)
        user_data.save()
        # email_address_data = request.POST['email_address_data']
        # password_data = request.POST['password_data']
        # companytype_data = request.POST['companytype_data']
        # title_data = request.POST['title_data']
        return redirect('register.html')
    
    return render(request,'register.html')