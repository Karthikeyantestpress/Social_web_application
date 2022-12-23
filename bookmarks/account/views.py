from .models import Profile
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm
from django.contrib import messages
from django.views.generic.edit import FormView
from .models import Profile


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
        Profile.objects.create(user=new_user)
        messages.success(
            self.request,
            "Registration successful you can login now to your account.",
        )
<<<<<<< HEAD
        return super().form_valid(form)
=======
    else:
        messages.error(
            request, "Unsuccessful registration. Invalid information."
        )
    return render(
        request, "account/register.html", {"form": UserRegistrationForm()}
    )


def register(request):
    if request.method == "POST":
        validate_the_registeration_form(request)
    return render(
        request, "account/register.html", {"form": UserRegistrationForm()}
    )


@login_required
def edit(request):
    user_form = UserEditForm(instance=request.user, data=request.POST or None)
    profile_form = ProfileEditForm(
        instance=request.user.profile,
        data=request.POST,
        files=request.FILES,
    )
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(
            request,
            "your profile has been updated successfully",
        )
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
>>>>>>> 9b891f6... support edit profile
