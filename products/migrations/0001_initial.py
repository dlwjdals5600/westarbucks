# Generated by Django 3.2.3 on 2021-05-23 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kca', models.DecimalField(decimal_places=3, max_digits=5)),
                ('sodium_mg', models.DecimalField(decimal_places=3, max_digits=5)),
                ('saturated_fat_g', models.DecimalField(decimal_places=3, max_digits=5)),
                ('sugars_g', models.DecimalField(decimal_places=3, max_digits=5)),
                ('protein_g', models.DecimalField(decimal_places=3, max_digits=5)),
                ('caffeine_mg', models.DecimalField(decimal_places=3, max_digits=5)),
                ('size_ml', models.CharField(max_length=50)),
                ('size_fluid_ounce', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'nutrition',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kr_name', models.CharField(max_length=50)),
                ('en_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.nutrition')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
    ]
