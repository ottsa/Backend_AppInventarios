# Generated by Django 4.2.3 on 2024-02-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insumo', '0009_alter_certificacion_registro_ica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadmedida',
            name='unidad',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
