from pyexpat import model
from django.db import models

class SumoInstance(models.Model):
    tag = models.TextField(primary_key=True)
    key = models.TextField()
    url = models.TextField()
