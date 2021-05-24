from django.db import models
from django.db.models.deletion import CASCADE



class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'menus'


class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'categories'


class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits = 6, decimal_places = 3)
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 3)
    saturated_fat_g = models.DecimalField(max_digits = 6, decimal_places = 3)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 3)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 3)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 3)
    size_ml = models.CharField(max_length=50)
    size_fluid_ounce = models.CharField(max_length=50)

    class Meta:
        db_table = 'nutritions'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    kr_name = models.CharField(max_length=40)
    en_name = models.CharField(max_length=50)
    description = models.TextField()
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_drink'


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'
        
class Allergy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'allergys'

class Allergy_product(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "allergys_product"