from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_code, name="submit_code"),
]
