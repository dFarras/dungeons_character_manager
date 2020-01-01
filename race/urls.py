from django.urls import path

from . import views

urlpatterns = [
    # ex: /race/
    path('race/', views.race, name='race'),
    # ex: /race/race.name/
    path('race/<str:race_name>/', views.race_detail, name='race_details'),
    # ex: /race/race.name/subrace.name/
    path('race/<str:race_name>/<str:subrace_name>/', views.subrace_detail, name='subrace_detail'),
]