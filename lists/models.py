from django.db import models

class Item(models.Model):
    name = models.TextField(default='')
    image = models.ImageField('labe
