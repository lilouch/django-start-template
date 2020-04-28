from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from PIL import Image as PILImg
from PIL import ImageEnhance as PILImageEnhance
from pathlib import Path
from .models import *
from django.conf import settings
from .forms import RecogForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse_lazy  # new

# Create your views here.


def home(request):
    return render(request, 'core/index.html')


class DashboardView(CreateView):
    model = Photo
    form_class = RecogForm
    template_name = 'core/dashboard.html'
    success_url = reverse_lazy('core:dashboard')


class ImagesListView(ListView):
    model = Photo
    template_name = "core/images_list.html"
    context_object_name = "images_list"


def dashboard(request):
    template = "core/dashboard.html"
    data = {}

    if request.POST:
        userform = RecogForm(request.POST, request.FILES)
        if userform.is_valid():
            print("VALID")
            origin_form = userform.cleaned_data["user_file"]
            origin_name = origin_form.name
            original_file = Path(settings.MEDIA_ROOT).joinpath(origin_name)
            thumb_name = original_file.stem + "_thumb.jpg"
            thumb_file = Path(settings.MEDIA_ROOT).joinpath(thumb_name)
            if original_file.is_file():
                original_file.unlink()
            if thumb_file.is_file():
                thumb_file.unlink()
            with open(original_file, 'wb+') as f:
                f.write(origin_form.read())
            origin_form.seek(0)
            # resize image
            image = PILImg.open(origin_form)
            image = image.resize((150, 150), PILImg.ANTIALIAS)
            # sharpness image
            image = PILImageEnhance.Sharpness(image)
            image = image.enhance(1.3)
            image.save(thumb_file, 'JPEG')
            data.update(origin_name=origin_name)
            data.update(thumb_name=thumb_name)
            userform = RecogForm()

            return render(request, template)
    else:
        userform = RecogForm()

    data.update(userform=userform)
    return render(request, template, data)
