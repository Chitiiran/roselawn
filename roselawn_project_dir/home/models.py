from django.db import models
import string, random

def generate_unique_name():
    length = 6
    while True:
        name = ''.join(random.choices(string.ascii_uppercase, k=length))
        if PortfolioItem.objects.filter(name=name) == 0:
            break
    return name

class PortfolioItem(models.Model):
    name = models.CharField(default="", max_length=6, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

class CustomerRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
