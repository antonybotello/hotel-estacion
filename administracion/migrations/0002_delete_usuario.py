# Generated by Django 4.1.1 on 2022-10-26 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0002_alter_pqrs_usuario_alter_respuestapqrs_usuario'),
        ('reserva', '0002_alter_reserva_usuario'),
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]