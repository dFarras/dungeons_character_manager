from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('items/light-weapons', views.light_weapons, name='light-weapons')
]
