from django.db import models
from misor_core.main import misor

class Community(models.Model):
    name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=200)


misor.set_misor(Community, Teacher)

print("Tables called")
