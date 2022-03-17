from django.db import models
from django.urls import reverse
from django.utils import timezone


class Service(models.Model):
    service_name = models.CharField(max_length=128)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class Worker(models.Model):
    worker_name = models.CharField(max_length=64)


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)


class OpeningHours(models.Model):
    day_name = models.CharField(max_length=32, unique=True)
    hours = models.CharField(max_length=32)

    def __str__(self):
        return self.day_name


class About(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()







