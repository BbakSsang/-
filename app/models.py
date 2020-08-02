from django.db import models

# Create your models here.
class Lol(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
