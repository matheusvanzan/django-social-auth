from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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

#     def test_that_fails(self):
#         self.assertTrue(False)
