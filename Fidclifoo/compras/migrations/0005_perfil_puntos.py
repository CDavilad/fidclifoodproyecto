# Generated by Django 4.0.2 on 2022-06-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_transaction_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
