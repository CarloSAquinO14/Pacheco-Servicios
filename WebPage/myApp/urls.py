from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/producto", views.producto, name="producto"),
    path("/servicios", views.servicios, name="servicios"),
    path("/contacto", views.contacto, name="contacto"),
    path("/inicio", views.inicio, name="inicio"),
]