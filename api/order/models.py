from django.db import models

from api.car.models import Car


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField(null=False)
    pickup_date = models.DateField(null=False)
    dropoff_date = models.DateField(null=False)
    pickup_location = models.CharField(max_length=50, null=False)
    dropoff_location = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20, null=False)
