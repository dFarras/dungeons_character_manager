from django.db import models
from . import dtos


class Weapon(models.Model):
    name = models.CharField(max_length=128)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
