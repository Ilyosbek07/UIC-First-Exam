from django.contrib.auth.models import User
from django.db import models

from apps.common.models import BaseModel


class Vacancy(BaseModel):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Resume(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_resume',
        on_delete=models.CASCADE
    )
    desc = models.TextField()

    def __str__(self):
        return self.user.username
