from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=256)

    