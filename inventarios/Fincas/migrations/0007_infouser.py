# Generated by Django 4.2.3 on 2023-09-08 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fincas', '0006_remove_finca_usuario_remove_lotes_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=150)),
                ('tipo_documento', models.CharField(max_length=20)),
                ('numero_documento', models.CharField(max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
