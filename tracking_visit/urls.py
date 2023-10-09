# urls.py

from django.urls import path
from .views import ListPointSales, AddVisit

urlpatterns = [
    path('list_point_sales/<str:number_phone>/', ListPointSales.as_view(), name='list_point_sales'),
    path('add_visit/<str:number_phone>/', AddVisit.as_view(), name='add_visit'),
]
