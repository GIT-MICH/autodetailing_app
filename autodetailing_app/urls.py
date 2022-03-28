from django.urls import path
from autodetailing_app.views import (MainView,
                                     CategoriesView,
                                     OutsideServicesView,
                                     InsideServicesView,
                                     AddServiceView,
                                     DeleteServiceView,
                                     AddOpinionView,
                                     AddWorkerView,
                                     ServicesView,
                                     ServiceDetailView,
                                     AddServiceToCartView,
                                     CreateOrderView,
                                     )

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('outside/', OutsideServicesView.as_view(), name='outside'),
    path('inside/', InsideServicesView.as_view(), name='inside'),
    path('add_service/', AddServiceView.as_view(), name='service-add'),
    path('del_service/<int:id>/', DeleteServiceView.as_view(), name='service-delete'),
    path('add_opinion/', AddOpinionView.as_view(), name='opinion-add'),
    path('add_worker/', AddWorkerView.as_view(), name='worker-add'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service/<int:id>', ServiceDetailView.as_view(), name='service-detail'),
    path('service_to_card/<int:service_id>/', AddServiceToCartView.as_view(), name='add-service-to-card'),
    path('order/', CreateOrderView.as_view(), name='order')

]