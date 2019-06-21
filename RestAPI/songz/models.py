from django.db import models

# Create your models here.

class Songz(models.Model):
    title = models.CharField(max_length=15)
    artist = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.artist} - {self.title}'