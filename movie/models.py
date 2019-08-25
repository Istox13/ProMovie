from django.db import models

# Create your models here.
class top(models.Model):
    title = models.CharField(max_length=100)
    poster = models.CharField(max_length=100)
    year = models.IntegerField()
    k_id = models.IntegerField()