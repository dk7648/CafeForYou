from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import OneToOneField

from cafeapp.models import Product, Cafe


class Order(models.Model):
    # name = models.CharField(max_length=60)
    # email = models.EmailField()
    # address = models.CharField(max_length=150)
    # postal_code = models.CharField(max_length=30)
    # city = models.CharField(max_length=100)
    user = OneToOneField(User, on_delete=models.CASCADE, related_name='order')
    cafe = OneToOneField(Cafe, on_delete=models.CASCADE, related_name='order', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity