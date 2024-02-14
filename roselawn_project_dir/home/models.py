from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

class CustomerRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
