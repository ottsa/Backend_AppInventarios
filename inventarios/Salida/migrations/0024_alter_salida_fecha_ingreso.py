# Generated by Django 4.2.3 on 2023-10-10 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salida', '0023_alter_salida_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 16, 30, 41, 438494)),
        ),
    ]