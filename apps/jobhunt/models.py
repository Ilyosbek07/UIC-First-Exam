from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
