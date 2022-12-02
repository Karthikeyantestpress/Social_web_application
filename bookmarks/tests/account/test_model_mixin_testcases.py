from django.test import TestCase
from django.contrib.auth.models import User


class ModelMixinTestcases(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john", password="johnpassword"
        )
