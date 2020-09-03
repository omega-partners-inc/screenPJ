from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
 

class User_data_Form(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = CustomUser
        fields = ['email','companytype','title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'