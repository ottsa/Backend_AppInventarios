# Generated by Django 4.2.3 on 2023-08-29 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0020_alter_entrada_fecha_ingreso_alter_entrada_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 18, 18, 50, 330860)),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalentrada',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 18, 18, 50, 330860)),
        ),
        migrations.AlterField(
            model_name='historicalentrada',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
    ]