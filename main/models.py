from django.db import models

# Create your models here.
class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True, verbose_name="Codigo estado")
    nombreEstado = models.CharField(max_length=30, verbose_name="Nombre estado")


class TipoRecibo(models.Model):
    idTipoRecibo = models.AutoField(primary_key=True, verbose_name="Codigo tipo recibo")
    nombreTipoRecibo = models.CharField(
        max_length=30, verbose_name="Nombre tipo recibo"
    )


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Codigo usuario")
    nombreUsuario = models.CharField(max_length=30, verbose_name="Nombre usuario")
    contraseniaUsuario = models.CharField(
        max_length=30, verbose_name="Contraseña usuario"
    )


class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True, verbose_name="Codigo empleado")
    nombresEmpleado = models.CharField(max_length=30, verbose_name="Nombre empleado")
    rutEmpleado = models.CharField(max_length=30, verbose_name="Rut empleado")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, verbose_name="Codigo cliente")
    nombresCliente = models.CharField(max_length=30, verbose_name="Nombre cliente")
    rutCliente = models.CharField(max_length=30, verbose_name="Rut cliente")
    domicilioCliente = models.CharField(max_length=85, verbose_name="Domicilio cliente")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True, verbose_name="Codigo proveedor")
    nombresProveedor = models.CharField(max_length=30, verbose_name="Nombre proveedor")
    rutProveedor = models.CharField(max_length=30, verbose_name="Rut proveedor")
    domicilioProveedor = models.CharField(
        max_length=85, verbose_name="Domicilio proveedor"
    )
    fonoProveedor = models.CharField(max_length=85, verbose_name="Fono proveedor")

    rubroProveedor = models.CharField(max_length=85, verbose_name="Rubro Proveedor")


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Codigo producto")
    nombreProducto = models.CharField(max_length=30, verbose_name="Nombre producto")
    stockProducto = models.IntegerField(verbose_name="Codigo producto")
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)


class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name="Codigo cliente")
    nombresServicio = models.CharField(max_length=30, verbose_name="Nombre cliente")
    idProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    idEstado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
