from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from django.views import View

from autodetailing_app.forms import AddServiceForm, AddOpinionForm
from autodetailing_app.models import Category, Service, About


class FirstView(View):
    def get(self, request):
        return render(request, 'autodetailing_app/base.html')


class MainView(View):
    def get(self, request):
        about = About.objects.get(id=1)
        return render(request, 'autodetailing_app/main.html', {'about': about})


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'autodetailing_app/base_with_navbar.html', {'categories': categories})


class AddServiceView(View):
    def get(self, request):
        form = AddServiceForm()
        return render(request, 'autodetailing_app/service_form.html', {'form': form})

    def post(self, request):
        form = AddServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return redirect('services')
        return render(request, 'autodetailing_app/service_form.html', {'form': form})


class AddOpinionView(View):
    def get(self, request):
        form = AddOpinionForm()
        return render(request, 'autodetailing_app/opinion_form.html', {'form': form})

    def post(self, request):
        form = AddOpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save()
            return redirect('main')
        return render(request, 'autodetailing_app/opinion_form.html', {'form': form})


class ServicesView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'autodetailing_app/services.html', {'services': services})


class ServiceDetailView(View):
    def get(self, request, id):
        service = Service.objects.get(id=id)
        # categories = Category.objects.all()
        return render(request, 'autodetailing_app/service_detail.html', {'service': service})
