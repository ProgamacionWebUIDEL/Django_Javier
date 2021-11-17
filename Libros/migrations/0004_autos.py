# Generated by Django 3.2.8 on 2021-11-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0003_auto_20211110_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Marca del Vehiculo', max_length=200)),
                ('cilindraje', models.FloatField(help_text='Cilindraje')),
            ],
        ),
    ]