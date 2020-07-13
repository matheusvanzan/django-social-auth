from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.urls import reverse


class UserLoginTest(TestCase):
    
    def setUp(self):
        User.objects.create_user('user', 'user@umcodigo.com', 'password')

    def tearDown(self):
        user = User.objects.get(username='user')
        user.delete()

    def test_login(self):
        user_a = User.objects.get(username='user')
        user_b = authenticate(username='user', password='password')
        self.assertEquals(user_a, user_b)
        
    # def test_index_view(self):
    #     user = User.objects.get(username='user')
    #     client = Client()
    #     client.login(username='user', password='password')
    #     response = client.get(reverse('index'))
        
    #     print(list(response.context)[0])
        
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(list(response.context)[0], {'user': user})
        
