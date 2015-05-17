from django.db import models
from time import time

def get_upload_file_name(instance, filename):
    return 'uploaded_files/%s_%s' % (str(time()).replace('.', '_'), filename)

class Item(models.Model):
    name = models.TextField(default='')
    # image = models.ImageField(upload_to='files/')
    image = models.FileField(upload_to=get_upload_file_name)
    parent = models.TextField(default='1')

