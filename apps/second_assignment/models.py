from django.contrib.auth.models import User
from django.db import models

from apps.common.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='company/')

    def __str__(self):
        return self.name


class Comment(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_comment',
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        related_name='company_comment',
        on_delete=models.CASCADE
    )

    rating = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    message = models.TextField()

    def __str__(self):
        return self.user.username


class Product(BaseModel):
    company = models.ForeignKey(
        Company,
        related_name='company_product',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
