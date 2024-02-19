from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50, null=False)
    day_rate = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    month_rate = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    image = models.CharField(max_length=256, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    location = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cars"
