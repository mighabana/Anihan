from django.db import models
from django.contrib.auth.models import User

class Produce(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    type = models.CharField(max_length=255)
    image_path = models.FilePathField()

class Farm(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Produce_Logs(models.Model):
    produce_id = models.ForeignKey('Produce', on_delete=models.CASCADE)
    farm_id = models.ForeignKey('Farm', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class OrderItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    produce_id = models.ForeignKey('Produce', on_delete=models.CASCADE)
    quantity= models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.IntegerField()

