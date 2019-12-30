from django.shortcuts import render, HttpResponse
from race.models import Race


# Create your views here.
def race(request):
    race_list = Race.objects.all
    #output = ', '.join([race.name for race in race_list])
    return render(request, 'race.html', {'race_list': race_list})


def index(request):
    latest_question_list = Race.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
