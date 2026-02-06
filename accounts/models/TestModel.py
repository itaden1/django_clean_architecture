from django.db import models

class TestModel(models.Model):
    foo = models.CharField(max_length=256)
