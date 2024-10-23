from django.shortcuts import render
from django.http import HttpResponse
from app.models import EmployeeModel
from app.serializer import EmployeeSerializer
from rest_framework import viewsets


class EmployeeViews(viewsets.ModelViewSet):
        queryset = EmployeeModel.objects.all()
        serializer_class = EmployeeSerializer
