

from rest_framework import serializers
from .models import Worker, PointSale, Visit

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class PointSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointSale
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
