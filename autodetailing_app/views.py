from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View

from autodetailing_app.forms import AddServiceForm, AddOpinionForm, AddWorkerForm, CartForm
from autodetailing_app.models import Category, Service, About, Cart


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
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect('main')
        return render(request, 'autodetailing_app/opinion_form.html', {'form': form})


class ServicesView(View):
    def get(self, request):
        services = Service.objects.all().order_by('name')
        return render(request, 'autodetailing_app/services.html', {'services': services})


class ServiceDetailView(View):
    def get(self, request, id):
        service = Service.objects.get(id=id)
        return render(request, 'autodetailing_app/service_detail.html', {'service': service})


class DeleteServiceView(View):
    def get(self, request, id):
        service = Service.objects.get(id=id)
        service.delete()
        return redirect('services')


class OutsideServicesView(View):
    def get(self, request):
        category = Category.objects.get(id=1)
        outside_services = Service.objects.filter(categories=1)
        return render(request, 'autodetailing_app/services_outside.html',
                      {'outside_services': outside_services, 'category': category})


class InsideServicesView(View):
    def get(self, request):
        category = Category.objects.get(id=2)
        inside_services = Service.objects.filter(categories=2)
        return render(request, 'autodetailing_app/services_inside.html',
                      {'inside_services': inside_services, 'category': category})


class AddWorkerView(View):
    def get(self, request):
        form = AddWorkerForm()
        return render(request, 'autodetailing_app/worker_form.html', {'form': form})

    def post(self, request):
        form = AddWorkerForm(request.POST)
        if form.is_valid():
            worker = form.save()
            return redirect('worker-add')
        return render(request, 'autodetailing_app/worker_form.html', {'form': form})


class CartView(View):
    def get(self, request):
        form = CartForm()
        services = Service.objects.all()
        return render(request, 'autodetailing_app/cart_form.html', {'form': form, 'services': services})

    def post(self, request):
        form = CartForm(request.POST)
        service = Service.objects.all()
        if form.is_valid():
            service = form.cleaned_data.get('service')
            worker = form.cleaned_data.get('worker')
            created = form.cleaned_data.get('created')
            user = request.user
            Cart.objects.create(service=service, worker=worker, created=created, user=user)
            return redirect('main')
        return render(request, 'autodetailing_app/cart_form.html', {'form': form})
