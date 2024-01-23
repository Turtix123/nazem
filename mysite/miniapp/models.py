from django.db import models

class datainsert(models.Model):
    title = models.CharField(max_length=200, default="x")
    name = models.CharField(max_length=200, default="x")
    play = models.CharField(max_length=200, default="x")


