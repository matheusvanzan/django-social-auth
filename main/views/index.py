from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from social_django.models import UserSocialAuth


class IndexView(LoginRequiredMixin, View):
    
    def get(self, request):
        
        data = { 'user': request.user }
        
        user_query = UserSocialAuth.objects.filter(user=request.user)
        if user_query.count():
            data.update({ 'social_user': user_query.first() })
        
        return render(request, 'main/index.html', data)
        