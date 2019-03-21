from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache

from extensionworkers.models import (
    Individual,
    Organization
)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
@never_cache
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@login_required
@never_cache
def individual(request, id):
    profile = get_object_or_404(Individual, pk=id)
    return render(request, 'individual.html', {'profile': profile})


def organization(request, id):
    profile = get_object_or_404(Organization, pk=id)
    return render(request, 'organization.html', {'profile': profile})


def url_redirect(request):
    return HttpResponsePermanentRedirect("/accounts/login/")
