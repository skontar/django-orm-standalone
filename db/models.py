from django.db import models
from manage import init_django

init_django()


class Model(models.Model):
    number = models.IntegerField()
