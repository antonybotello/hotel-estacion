# Generated by Django 4.1.1 on 2022-10-26 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0004_tipohabitacion_complementostipohabitacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitacion',
            old_name='TipoHabitacion',
            new_name='tipoHabitacion',
        ),
    ]