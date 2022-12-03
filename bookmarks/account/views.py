from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def settings(request):
    return render(request, "account/settings.html")
