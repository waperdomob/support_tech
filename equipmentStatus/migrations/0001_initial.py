# Generated by Django 4.0.4 on 2023-07-28 22:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de ingreso')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(max_length=45)),
                ('estado', models.CharField(max_length=45)),
                ('diagnostico', models.TextField()),
                ('reporte_ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipmentStatus.ingreso')),
            ],
        ),
    ]
