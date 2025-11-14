from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="addon1_home"),
] 