from django.db import models
from django.utils import timezone

# Create your models here.

class Islaidu_tipai(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=100)
    aktyvus = models.BooleanField(default=False)

    class Meta:
        ordering = ['-aktyvus']
        verbose_name = 'Išlaidų tipas'
        verbose_name_plural = 'Išlaidų tipai'

    def __str__(self):
        return self.pavadinimas

class Islaidos(models.Model):
    data = models.DateField('Data', default=timezone.now)
    tipas = models.ForeignKey(Islaidu_tipai, on_delete=models.CASCADE, null=True, blank=True)
    tiekejas = models.CharField('Tiekėjas', max_length=50)
    dokumento_nr = models.CharField('Dokumento numeris', max_length=15)
    suma = models.FloatField('Suma', max_length=100)

    class Meta:
        ordering = ['-data']
        verbose_name = 'Išlaidos'
        verbose_name_plural = 'Išlaidos'

    def __str__(self):
        return self.tiekejas