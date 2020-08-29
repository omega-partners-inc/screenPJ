from django import forms
from .models import CustomUser
 
 
class User_data_Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'companytype', 'title']
