# Generated by Django 3.2.3 on 2021-05-23 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_allergy_allergy_product'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='allergy',
            table='allergys',
        ),
        migrations.AlterModelTable(
            name='allergy_product',
            table='allerty_products',
        ),
    ]
