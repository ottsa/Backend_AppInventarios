# Generated by Django 4.2.3 on 2023-09-07 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salida', '0019_alter_salida_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 7, 27, 36, 870930)),
        ),
    ]