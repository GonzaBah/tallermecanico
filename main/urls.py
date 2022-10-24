from django.urls import path
from .views import inicio, productos

urlpatterns = [
    path("productos/", productos, name="productos"),
]
