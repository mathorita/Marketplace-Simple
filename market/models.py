from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available_quantity = models.IntegerField()
    owner = models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    buyer = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='order_products',on_delete=models.CASCADE)
    quantity =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)