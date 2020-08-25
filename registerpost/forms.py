from django import forms
from .models import User_data
 
 
class User_data_Form(forms.ModelForm):
    class Meta:
        model = User_data
        fields = ['email_address_data', 'password_data', 'companytype_data', 'title_data']

