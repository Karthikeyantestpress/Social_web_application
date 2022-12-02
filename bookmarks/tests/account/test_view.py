from django.test import TestCase
from django.urls import reverse
from .test_model_mixin_testcases import ModelMixinTestcases


class UserLoginView(ModelMixinTestcases, TestCase):
    def test_template_used_with_dashboard(self):

        self.client.login(username="john", password="johnpassword")
        response = self.client.get(reverse("dashboard"))

        self.assertTemplateUsed(response, "account/dashboard.html")
