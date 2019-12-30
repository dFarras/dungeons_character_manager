from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('race/', views.race, name='race'),
    # ex: /polls/5/
    path('race/<str:race_name>/', views.detail, name='detail'),
]