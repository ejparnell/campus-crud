from rest_framework import serializers

from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Doctor