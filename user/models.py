
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import AbstractUser


MEMBERSHIP_CHOICES = (
    ('F', 'free_trial'),
    ('M', 'member'),
    ('N', 'not_member')
)


class UserLibraryImages(models.Model):
    images = models.ManyToManyField('Image')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def image_list(self):
        return self.images.all()

    class Meta:
        verbose_name = 'User Library'
        verbose_name_plural = 'User Library'

#If the user just created we create the user library images
def post_user_signup_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserLibraryImages.objects.get_or_create(user=instance)

#When the user is save, we call the post_user_signup_receiver
#If no sender, it will be call for every single model
post_save.connect(post_user_signup_receiver, sender=settings.AUTH_USER_MODEL )


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class User(AbstractUser):
    is_member = models.BooleanField(default=False)
    on_free_trial = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    stripe_subscription_id = models.CharField(
        max_length=40, blank=True, null=True)
    stripe_subscription_item_id = models.CharField(
        max_length=40, blank=True, null=True)

    def __str__(self):
        return self.user.username
