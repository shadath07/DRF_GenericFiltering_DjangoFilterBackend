from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
# To filter uisng the views 
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # To filter using the views 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']
