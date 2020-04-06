
from django.db import models

from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone



class File(models.Model):
    file = models.ImageField()

    def __str__(self):
        return self.file.name


