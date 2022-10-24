#!/usr/bin/env python3
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Producto
from .models import Servicio


@receiver(post_save, sender=Producto)
def checkear_stock(sender, instance, update_fields, **kwargs):
    if update_fields:
        stock = instance.objects.get(stockProducto)
        if stock == 0:
            servicio = Servicio.objects.get(idProducto=instance.idProducto)
            servicio.idEstado = 1
            servicio.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
