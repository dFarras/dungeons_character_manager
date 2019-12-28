from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('items/weapons', views.weapons, name='weapons')
]
