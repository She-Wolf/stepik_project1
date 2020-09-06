from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View


class MainView(View):
    template_name = 'index.html'
    # model = Author


class DepartureView(View):
    template_name = 'departure.html'


class TourView(View):
    template_name = 'tour.html'

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Пинганите разраба')

def custom_handler500(request, exception):
    return HttpResponseNotFound('Сервер прилег... Скоро починим')