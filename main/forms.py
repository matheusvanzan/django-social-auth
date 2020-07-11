from django import forms


class UserForm(forms.Form):
    
    username = forms.CharField(label = 'Usuário')
    password = forms.CharField(label = 'Senha', widget = forms.PasswordInput)