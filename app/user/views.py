from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from .models import *




# Create your views here.
class UserDetailsView(View):
    pass

class UserDeleteView(View):
    pass


class UserUpdateView(View):
    pass


class UserCreateView(View):
    pass


def profile_view(request):
    return render(request, "user/profile.html", {} )
