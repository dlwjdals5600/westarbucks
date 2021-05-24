# Generated by Django 3.2.3 on 2021-05-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210523_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='caffeine_mg',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='one_serving_kca',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='protein_g',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='saturated_fat_g',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sodium_mg',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sugars_g',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
