from django.db import models
from ..product.models import Product

class Sensor(models.Model) :
    sensor_id = models.IntegerField()
    product_id = models.OneToOneField(Product,on_delete=models.DO_NOTHING())

    # def __str__(self):
    #     return self.

# Create your models here.
