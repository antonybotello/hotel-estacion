# Generated by Django 4.1.1 on 2022-11-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0015_alter_tipohabitacion_nombretipohabitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipohabitacion',
            name='nombreTipoHabitacion',
            field=models.CharField(choices=[('Sencilla', 'Sencilla'), ('Doble', 'Doble'), ('Campestre', 'Campestre')], default='Sencilla', max_length=10, verbose_name='Nombre Tipo de Habitacion'),
        ),
    ]