
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

# Tipo Habitacion.
class TipoHabitacion(models.Model):
    class NombreTipoHabitacion(models.TextChoices):
        Sencilla = 'Sencilla', _('Sencilla')
        Doble = 'Doble', _('Doble')
        Campestre = 'Campestre', _('Campestre')
    nombreTipoHabitacion = models.CharField(max_length=10, choices=NombreTipoHabitacion.choices,
                                            default=NombreTipoHabitacion.Sencilla, verbose_name="Nombre Tipo de Habitacion")
    complementosTipoHabitacion = models.CharField(
        max_length=50, verbose_name="Complementos Tipo Habitacion")
    valorTipoHabitacion = models.IntegerField(
        verbose_name="Valor Tipo Habitacion")
    descripcionTipoHabitacion = models.CharField(
        max_length=200, verbose_name="Descripcion Tipo Habitacion")
    capacidad = models.CharField(max_length=45, verbose_name="Capacidad")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self):
        return "%s " % (self.nombreTipoHabitacion)


# Habitacion.
class Habitacion(models.Model):
    numeroHabitacion = models.CharField(
        max_length=4, verbose_name="Numero de Habitacion")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class Disponibilidad(models.TextChoices):
        DISPONIBLE = 'Disponible', _('Disponible')
        OCUPADA = 'Ocupada', _('Ocupada')

    disponibilidad = models.CharField(max_length=10, choices=Disponibilidad.choices,
                                      default=Disponibilidad.DISPONIBLE, verbose_name="Disponibilidad")
    tipoHabitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE, verbose_name="Tipo Habitacion")

    class Sede(models.TextChoices):
        ESTACION = 'estacion', _('La Estación')
        BOSQUE = 'bosque', _('El Bosque')
    sede = models.CharField(
        max_length=8, choices=Sede.choices, default=Sede.ESTACION, verbose_name="Sede")

    def __str__(self):
        return "Habitación %s" % (self.numeroHabitacion)
