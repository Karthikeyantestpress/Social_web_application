from django.test import TestCase
from django.urls import reverse, resolve
from account.views import dashboard, settings, register, edit


class UserLogin(TestCase):
    def test_user_dashboard_url(self):

        user_dashboard_url = reverse("dashboard")
        self.assertEqual((resolve(user_dashboard_url).func), dashboard)

    def test_settings_url(self):

        settings_url = reverse("settings")
        self.assertEqual((resolve(settings_url).func), settings)

    def test_register_url(self):

        register_url = reverse("register")
        self.assertEqual((resolve(register_url).func), register)

    def test_edit_url(self):

        edit_url = reverse("edit")
        self.assertEqual((resolve(edit_url).func), edit)
