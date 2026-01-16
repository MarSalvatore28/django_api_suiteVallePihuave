from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Ruta vacía para la raíz
    path("index/", views.index, name="index-alt"),  # Alternativa con /index/
]