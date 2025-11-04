from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("estimar/", views.estimar_precio_casa, name="estimar_precio_casa"),
    path("dataset/", views.dataset_info, name="dataset_info"),
]
