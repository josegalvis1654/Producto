# Generated by Django 5.1.1 on 2024-11-09 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0004_rename_estado_estado_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='proveedor',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
