# Generated by Django 3.2.8 on 2021-11-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0002_libro_numero_pag'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.CharField(default=1, help_text='Editorial', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='isbn',
            field=models.CharField(default=1, help_text='Código de Barras', max_length=20),
            preserve_default=False,
        ),
    ]
