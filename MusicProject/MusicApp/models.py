from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Audio(models.Model):
    audio_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    upload = models.FileField(upload_to='audio/')
    def __str__(self):
        return self.name

# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to='file/')