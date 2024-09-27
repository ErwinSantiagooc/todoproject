from django.db import models

# Create your models here.
class ProductType(models.Model):
    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive")
                
       ]
    
    name=models.CharField(max_length=511, null=False)
    status = models.CharField(max_length=55, choices=STATUSES, default="active")

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive")
                
       ]
    name=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    product_type=models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(max_length=55, choices=STATUSES, default="active")
    
    def __str__(self) -> str:
        return self.name
    
class Client(models.Model):
    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive")
                
       ]
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=55, choices=STATUSES, default="active")
    
    def __str__(self) -> str:
        return self.name