from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseServerError
from django.views import View
from data import tours, departures


class MainView(View):
    def get(self, request):
        return render(request, 'index.html')


class DepartureView(View):
    def get(self, request, departure):
        if departure not in departures.keys():
            raise Http404

        context = {
            "departure": departures[departure]
        }
        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, tour):
        if tour not in tours.keys():
            raise Http404

        context = {
            "tours": tours.tour
        }

        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, нет такой страницы...Проверьте, что ввели ')


def custom_handler500(exception):
    return HttpResponseServerError('Сервер прилег... Скоро починим')