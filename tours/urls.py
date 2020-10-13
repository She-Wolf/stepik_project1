from django.urls import path

from tours import views

urlpatterns = [
    path('', views.index, name='home'),
    path('departure/<str:departure_id>/', views.departure, name='departure'),
    path('tours/<int:tour_id>/', views.tour, name='tour'),
]
