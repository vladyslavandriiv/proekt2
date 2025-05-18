from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    medical_history = models.TextField(blank=True)  # нове поле для історії хвороб

    def __str__(self):
        return f"{self.name} ({self.species})"


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Visit(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    visit_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.visit_date} – {self.animal.name}"
