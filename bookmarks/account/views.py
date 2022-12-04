from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views.generic.edit import FormView


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def settings(request):
    return render(request, "account/settings.html")


class UserRegistrationForm(FormView):
    template_name = "account/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()
        messages.success(
            self.request,
            "Registration successful you can login now to your account.",
        )
        return super().form_valid(form)
