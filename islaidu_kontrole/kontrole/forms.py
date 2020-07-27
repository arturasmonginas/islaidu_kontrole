from django.forms import ModelForm
from .models import Islaidos, Islaidu_tipai

class Prideti(ModelForm):
    class Meta:
        model = Islaidos
        fields = ['data', 'tipas', 'tiekejas', 'dokumento_nr', 'suma']

class PridetiTipa(ModelForm):
    class Meta:
        model = Islaidu_tipai
        fields = ['pavadinimas', 'aktyvus']