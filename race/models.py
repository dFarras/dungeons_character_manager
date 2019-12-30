from django.db import models


# Create your models here.
class CharImprovements(models.Model):
    stat = models.CharField(max_length=3)
    bonus = models.IntegerField()


class SubRace(models.Model):
    name = models.CharField(max_length=32, default='default')
    char_improvements = models.ManyToManyField(CharImprovements)


class Race(models.Model):
    name = models.CharField(max_length=32, default='default')
    char_improvements = models.ManyToManyField(CharImprovements)
    alignment = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    speed = models.IntegerField()
    sub_races = models.ForeignKey(SubRace, on_delete=models.CASCADE, null=True)
