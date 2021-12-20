from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
from django import forms


class UsedFor(models.Model):
    title = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    levels = [
        ("top", 'Top'),
        ("medium", 'Medium'),
        ('normal', 'Normal',)
    ]
    title = models.CharField(max_length=255, null=True)
    level = models.CharField(max_length=200, choices=levels, null=True)
    details = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    code = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    usedFor = models.ForeignKey(UsedFor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductDetails(models.Model):
    sizes = [
        ("XL", "Extra Large"),
        ("L", "Large"),
        ("M", "Medium"),
        ("SM", "Small"),
        ("XSM", "Extra Small")
    ]
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name="product_ID")
    price = models.IntegerField()
    color = models.CharField(max_length=244)
    size = models.CharField(max_length=50, choices=sizes)
    quantity = models.CharField(max_length=244)
    weight = models.CharField(max_length=244)
    discount = models.IntegerField(help_text=" Entered value will be in %")

    def __str__(self):
        return self.product.title


class ProductTest(models.Model):
    name = models.CharField(max_length=232)
    brand = models.CharField(max_length=232)
    size = models.CharField(max_length=232)

    def __str__(self):
        return self.name


class ImageLibrary(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    image = models.ImageField(upload_to='product/Images')

    def __str__(self):
        return self.product.title

# class Product_ratings(models.Model):
#     p_id = models.ForeignKey(
#         Product, on_delete=models.CASCADE, to_field='product_id')
#     comment = models.CharField(max_length=200, null=True, blank=True)
#     rating = models.IntegerField(null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
