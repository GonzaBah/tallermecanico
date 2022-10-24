from django.contrib import admin
from .models import (
    Estado,
    TipoRecibo,
    Recibo,
    Usuario,
    Empleado,
    Cliente,
    Proveedor,
    Producto,
    Servicio,
    Pedido,
    ServicioCliente,
)

# Register your models here.
admin.site.register(Estado)
admin.site.register(TipoRecibo)
admin.site.register(Recibo)
admin.site.register(Usuario)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Pedido)
admin.site.register(ServicioCliente)
