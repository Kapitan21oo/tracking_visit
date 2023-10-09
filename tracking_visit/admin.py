from django.contrib import admin
from .models import Worker, PointSale, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number_phone')
    search_fields = ('name',)
    list_editable = ('name', 'number_phone')

@admin.register(PointSale)
class PointSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'worker')
    search_fields = ('title',)
    list_filter = ('worker',)
    list_editable = ('title', 'worker')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'point_sale', 'latitude', 'longitude')
    search_fields = ('point_sale__title', 'point_sale__worker__name')
    list_filter = ('point_sale__worker', 'point_sale',)
