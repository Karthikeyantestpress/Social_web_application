from django.test import TestCase
from .test_model_mixin_testcases import ModelMixinTestcases
from django.urls import reverse
from django.contrib.auth.models import User
from account.forms import LoginForm


class UserLoginView(ModelMixinTestcases, TestCase):
    def test_templates_used_with_user_login(self):

        response = self.client.get(reverse("account:login"))
        self.assertTemplateUsed(response, "account/login.html")

    def test_user_login_returns_loginform(self):

        response = self.client.get(reverse("account:login"))
        self.assertIsInstance(response.context.get("form"), LoginForm)

    def test_login_succeeds_with_valid_credentials(self):

        response = self.client.post(
            reverse("account:login"),
            {"username": "john", "password": "johnpassword"},
        )
        self.assertEqual(
            response.content.decode(), "Authenticated successfully"
        )

    def test_login_fails_with_invalid_credentials(self):

        response = self.client.post(
            reverse("account:login"),
            {"username": "Invalid_name", "password": "Invalid_password"},
        )
        self.assertEqual(response.content.decode(), "Invalid login")

    def test_login_fails_when_account_is_inactive(self):
        self.user.is_active = False
        self.user.save()

        response = self.client.post(
            reverse("account:login"),
            {"username": "john", "password": "johnpassword"},
        )
        self.assertEqual(
            response.content.decode(),
            "Account has been disabled please try any other account",
        )
