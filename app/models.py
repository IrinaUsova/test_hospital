from django.conf import settings
from django.db import models
from django.utils import timezone


class Department(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    adress = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

class Doctor(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Patient(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


