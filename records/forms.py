from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Animal, Doctor, Visit

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'age', 'weight', 'height', 'medical_history']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'contact_info']


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['animal', 'doctor', 'visit_date', 'notes']
