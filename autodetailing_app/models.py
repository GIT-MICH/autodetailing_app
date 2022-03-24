from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa usługi')
    image = models.ImageField(blank=True, null=True, verbose_name='Dodaj plik')
    description = models.TextField(verbose_name='Opis')
    duration = models.IntegerField(verbose_name='Czas wykonania (min.)')
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.FloatField(verbose_name='Cena (zł)')
    categories = models.ManyToManyField('Category')

    def get_absolute_url(self):
        return reverse('service-detail', args=(self.id,))

    def remove_url(self):
        return reverse('service-delete', args=(self.id,))

    def upper_name(self):
        return self.name.upper()

    def min_to_hours(self):
        return self.duration / 60

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None)
    created = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# class OpeningHours(models.Model):
#     day_name = models.CharField(max_length=32, unique=True)
#     hours = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.day_name


class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=64)
    description = models.TextField()


class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
