# views.py

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker, PointSale, Visit
from .serializers import WorkerSerializer, PointSaleSerializer, VisitSerializer

class ListPointSales(APIView):
    def get(self, request, number_phone):
        worker = get_object_or_404(Worker, number_phone=number_phone)
        point_sales = PointSale.objects.filter(worker=worker)
        serializer = PointSaleSerializer(point_sales, many=True)
        return Response(serializer.data)

class AddVisit(APIView):
    def post(self, request, number_phone):
        worker = get_object_or_404(Worker, number_phone=number_phone)

        # Получение данных из запроса
        point_sale_pk = request.data.get('point_sale_pk')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if latitude is not None and longitude is not None:
            # Проверка, что переданный номер телефона Работника привязан к указанной ТТ
            point_sale = get_object_or_404(PointSale, pk=point_sale_pk, worker=worker)

            # Создание Посещения
            visit = Visit.objects.create(
                point_sale=point_sale,
                latitude=latitude,
                longitude=longitude
            )

            serializer = VisitSerializer(visit)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid coordinates format"}, status=status.HTTP_400_BAD_REQUEST)

