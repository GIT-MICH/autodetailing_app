from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


def get_absolute_url(self):
    return reverse('service-detail', args=(self.id,))


class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa usługi')
    image = models.ImageField(blank=True, null=True, verbose_name='Dodaj plik')
    description = models.TextField(verbose_name='Opis')
    duration = models.IntegerField(verbose_name='Czas wykonania (min.)', default=0)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.FloatField(verbose_name='Cena (zł)', default=0)
    categories = models.ManyToManyField('Category')

    class Meta:
        verbose_name = 'Usługa'
        verbose_name_plural = 'Usługi'

    def get_absolute_url(self):
        return reverse('service-detail', args=(self.id,))

    def remove_url(self):
        return reverse('service-delete', args=(self.id,))

    def add_to_card_url(self):
        return reverse('add-service-to-card', args=(self.id,))

    def remove_service_url(self):
        return reverse('remove-service', args=(self.id,))

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

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


class Worker(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pracownik'
        verbose_name_plural = 'Pracownicy'


class Cart(models.Model):
    services = models.ManyToManyField(Service)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None, null=True)
    meeting_date = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return ", ".join([str(t) for t in self.services.all()])

    def get_total_value(self):
        suma = 0
        for service in self.services.all():
            suma += service.price
        return suma

    def get_total_time(self):
        total = 0
        for service in self.services.all():
            total += service.duration
        return round(total / 60, 0)

    class Meta:
        verbose_name = 'Koszyk'
        verbose_name_plural = 'Koszyk'


class Order(models.Model):
    services = models.ManyToManyField(Service, verbose_name='Zamówienia')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None, null=True, verbose_name='Pracownik')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    meeting_date = models.DateField(null=True, verbose_name='Dzień')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Użytkownik')
    is_done = models.BooleanField(default=False, verbose_name="Czy zamówienie zostało zrealizowane?")

    def __str__(self):
        return ", ".join([str(t) for t in self.services.all()])

    class Meta:
        verbose_name = 'Zamówienie'
        verbose_name_plural = 'Zamówienia'

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

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Opinia'
        verbose_name_plural = 'Opinie'


class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

