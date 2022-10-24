from django.urls import path
from .views import inicio, productos, stock

urlpatterns = [
    path("productos/", productos, name="productos"),
    path('productos/stock_<int:id>_<int:num>', stock, name="stock")
]
