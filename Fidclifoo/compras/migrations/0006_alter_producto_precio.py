# Generated by Django 4.0.2 on 2022-06-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_perfil_puntos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
