# Generated by Django 5.1.1 on 2024-11-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0002_alter_lote_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='FechaCaducidad',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='FechaEntrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]