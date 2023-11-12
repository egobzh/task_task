from django.db import models
from datetime import date

class Tasks(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=date.today())
    updated_date = models.DateTimeField(default=date.today())
    scheduled_date = models.DateTimeField(default=None, null=True)

