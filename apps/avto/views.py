from django.shortcuts import render
from rest_framework import generics

from apps.avto.models import Announcement
from apps.avto.serializers import AutoSerializer


class AnnouncementRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AutoSerializer
