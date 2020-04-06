from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
	return render(request, 'core/index.html')


def dashboard(request):
	return render(request, 'core/dashboard.html')