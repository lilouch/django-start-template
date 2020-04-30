from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('account/profile/', views.profile_view, name="profile"),
]
