from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserLibraryImages, Image

admin.site.register(Image)
admin.site.register(User, UserAdmin)
admin.site.register(UserLibraryImages)
