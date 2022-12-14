from django.test import TestCase
from django.urls import reverse, resolve
from account.views import user_login


class UserLogin(TestCase):
    def test_user_login_url(self):

        user_login_url = reverse("account:login")
        self.assertEqual((resolve(user_login_url).func), user_login)
