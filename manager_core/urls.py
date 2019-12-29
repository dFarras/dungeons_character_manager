from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('weapons', views.weapons, name='weapons')
]
