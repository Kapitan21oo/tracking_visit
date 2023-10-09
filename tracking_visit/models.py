from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)
    number_phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' / ' + self.number_phone


class PointSale(models.Model):
    title = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    point_sale = models.ForeignKey(PointSale, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
