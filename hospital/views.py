from django.shortcuts import render, get_object_or_404
from hospital.serializers import DoctorSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Doctor

# Create your views here.
class DoctorsView(APIView):
    """View class for hospital/ for viewing all docs and creating docs"""
    def get(self, request):
        docs = Doctor.objects.all()
        serializer = DoctorSerializer(docs, many=True)
        return Response({'docs': serializer.data})


class DoctorDetailView(APIView):
    """View class for hospital/:pk for viewing a single doc, updating a single doc, or remoing a single doc"""