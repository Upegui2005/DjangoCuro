# Generated by Django 4.2.4 on 2023-12-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='coleccion',
            field=models.IntegerField(choices=[('1', 'Curandera')], default='1'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='rol',
            field=models.IntegerField(choices=[('1', 'Administrador'), ('2', 'Usuario')], default='2'),
        ),
    ]