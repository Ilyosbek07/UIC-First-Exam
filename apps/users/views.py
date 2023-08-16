from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from apps.users.serializers import RegisterUserSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
