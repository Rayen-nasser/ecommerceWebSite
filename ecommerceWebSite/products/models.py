from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)  # Increased max_length for email
    profile = models.TextField(blank=True)  # Fixed typo: `black=True` to `blank=True`
    photo = models.ImageField(upload_to='seller/photos/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Using DecimalField for price
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photos/')

    def __str__(self):
        return self.name
