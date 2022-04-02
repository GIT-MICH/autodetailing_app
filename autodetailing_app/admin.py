from django.contrib import admin
from autodetailing_app.models import Service, Category, Worker, Order, Cart, Opinion


def is_done(model_admin, request, query_set):
    query_set.update(is_done=True)


is_done.short_description = "Zamówienie zrealizowane !"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def services(obj):
        return ", ".join([str(t) for t in obj.services.all()])

    actions = [is_done, ]
    list_display = (services, 'worker', 'meeting_date', 'user', 'is_done')


admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Worker)
admin.site.register(Cart)
admin.site.register(Opinion)
