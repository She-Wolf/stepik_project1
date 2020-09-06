
from django.contrib import admin
from django.urls import path
from stepik_tours.tours.views import MainView, DepartureView, TourView
from stepik_tours.tours.views import custom_handler404
from stepik_tours.tours.views import custom_handler500
handler500 = custom_handler500
handler404 = custom_handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', MainView.as_view()),
    path('/departure/<str:departure>/', DepartureView.as_view()),
    path('/tour/<int:id>/', TourView.as_view()),
]
