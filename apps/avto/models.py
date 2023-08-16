from django.db import models

from apps.common.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Type(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Announcement(BaseModel):
    brand = models.ForeignKey(
        Brand,
        related_name='brand',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Type,
        related_name='brand',
        on_delete=models.CASCADE
    )
    price = models.IntegerField()

    def __str__(self):
        return self.type.name
