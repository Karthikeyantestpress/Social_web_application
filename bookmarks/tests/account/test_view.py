from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from account.forms import UserRegistrationForm
from .test_model_mixin_testcases import ModelMixinTestcases


class UserLoginView(ModelMixinTestcases, TestCase):
    def test_template_used_with_dashboard(self):

        self.client.login(username="john", password="johnpassword")
        response = self.client.get(reverse("dashboard"))

        self.assertTemplateUsed(response, "account/dashboard.html")

    def test_template_used_with_settings(self):

        response = self.client.get(reverse("settings"))

        self.assertTemplateUsed(response, "account/settings.html")

    def test_templates_used_with_register_account(self):

        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(
            response, "account/register.html", "account/register_done.html"
        )

    def test_user_regiter_returns_registrationform(self):
        response = self.client.get(reverse("register"))

        self.assertIsInstance(
            response.context.get("form"), UserRegistrationForm
        )

    def test_register_succeeds_registering_users_with_valid_credentials(self):
        self.client.post(
            reverse("register"),
            data={
                "username": "karthikeyan",
                "first_name": "karthik",
                "email": "karthiktest51@gmail.com",
                "password": "123@Kar",
                "password2": "123@Kar",
            },
        )
        self.assertTrue(User.objects.filter(username="karthikeyan").exists())

    def test_template_used_with_edit_profile(self):
        self.client.login(username="john", password="johnpassword")
        response = self.client.get(reverse("edit"))

        self.assertTemplateUsed(response, "account/edit.html")

    def test_editing_user_profile_succeds(self):

        self.client.login(username="john", password="johnpassword")
        self.client.post(
            reverse("edit"),
            data={
                "first_name": "johncena",
            },
        )
        user = User.objects.get(id=1)
        username = user.first_name
        self.assertEqual(username, "johncena")


class UserListView(ModelMixinTestcases, TestCase):
    def test_template_used_with_user_list_view(self):

        self.client.login(username="john", password="johnpassword")
        response = self.client.get(reverse("user_list"))

        self.assertTemplateUsed(response, "account/user/list.html")
