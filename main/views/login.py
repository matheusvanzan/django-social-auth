from django.shortcuts import render
from django.views import View
from django.forms import Form
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from main.forms import UserForm


class LoginView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        
        data = {
            'form': UserForm()
        }
        
        return render(request, 'main/login.html', data)
        
    def post(self, request):
        
        form = UserForm(data=request.POST)
        

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password:
                user = authenticate(username=username, password=password)

                if user:
                    login(request, user)
                    print('user', user)
                    return HttpResponseRedirect(reverse('index'))
        
        return HttpResponseRedirect(reverse('login'))