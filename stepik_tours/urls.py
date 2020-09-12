from django.contrib import admin
from django.urls import path

from tours.views import custom_handler404
from tours.views import custom_handler500
from tours.views import MainView, DepartureView, TourView

handler500 = custom_handler500
handler404 = custom_handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tours/<int:tour_id>/', TourView.as_view(), name='tour'),
]
