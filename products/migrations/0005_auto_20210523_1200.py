# Generated by Django 3.2.3 on 2021-05-23 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210523_1110'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='allergy_product',
            table='allergys_product',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products_drink',
        ),
    ]