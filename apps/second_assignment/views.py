from django.shortcuts import render
from rest_framework import generics

from apps.second_assignment.models import Company, Comment
from apps.second_assignment.serializers import CompanyCommentSerializer, CompanyProductsSerializer


class CompanyCommentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCommentSerializer


class CompanyProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyProductsSerializer
