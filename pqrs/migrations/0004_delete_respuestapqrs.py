# Generated by Django 4.1.1 on 2022-10-31 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0003_remove_pqrs_usuario_remove_respuestapqrs_usuario_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RespuestaPQRS',
        ),
    ]