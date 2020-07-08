from django.forms import ModelForm, Form
from django.contrib.auth.models import User as DjangoUser


class DjangoUserForm(ModelForm):
    
    class Meta:
        model = DjangoUser
        fields = ['username', 'password']