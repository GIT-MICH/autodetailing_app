"""PROJEKT_KONCOWY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from autodetailing_app.views import (MainView,
                                     FirstView,
                                     CategoriesView,
                                     OutsideServicesView,
                                     InsideServicesView,
                                     AddServiceView,
                                     AddOpinionView,
                                     AddWorkerView,
                                     ServicesView,
                                     ServiceDetailView,
                                     CartView,
                                     )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FirstView.as_view(), name='base'),
    path('main/', MainView.as_view(), name='main'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('outside/', OutsideServicesView.as_view(), name='outside'),
    path('inside/', InsideServicesView.as_view(), name='inside'),
    path('add_service/', AddServiceView.as_view(), name='service-add'),
    path('add_opinion/', AddOpinionView.as_view(), name='opinion-add'),
    path('add_worker/', AddWorkerView.as_view(), name='worker-add'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service/<int:id>', ServiceDetailView.as_view(), name='service-detail'),
    path('cart/', CartView.as_view(), name='cart')

]
