# Base Imports

# Third Party Imports
from django.db import models


# Application Imports


class BaseModel(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class City(BaseModel):
    name = models.CharField(max_length=60, unique=True)
    country = models.CharField(max_length=60)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
