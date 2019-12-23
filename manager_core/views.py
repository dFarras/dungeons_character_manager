from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This view is intended to show characters sheet.")


def light_weapons(request):
    return HttpResponse("This view is intended to show all light weapons loaded in the system")
