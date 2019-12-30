from django.shortcuts import render, HttpResponse
from race.models import Race


# Create your views here.
def race(request):
    race_list = Race.objects.all
    return render(request, 'race.html', {'race_list': race_list})


def detail(request, race_name):
    race = Race.objects.get(name=race_name)
    return render(request, 'race_details.html', {'race': race})