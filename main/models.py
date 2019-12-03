from django.db import models


class RDV(models.Model):
    date = models.DateTimeField()
    description = models.TextField()