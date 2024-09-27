from django.contrib import admin
from .models import ProductType, Product, Client, Credit, Payment
# Register your models here.

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Credit)
admin.site.register(Payment)