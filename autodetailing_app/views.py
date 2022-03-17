from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from django.views import View


class Base(View):
    def get(self, request):
        message = 'Widok do zaimplementowania!'
        return render(request,
                      'autodetailing_app/base.html',
                      {'message': message}
                      )


