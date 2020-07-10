from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

        
class LogoutView(LoginRequiredMixin, View):
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

        