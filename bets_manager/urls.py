from django.urls import path

from bets_manager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.index, name='about'),
]
