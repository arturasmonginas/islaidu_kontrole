from django.shortcuts import render, redirect
from .models import Islaidos
from django.db.models import Sum
from .forms import Prideti, PridetiTipa


# Create your views here.
def index(request):
    suma_sum = Islaidos.objects.aggregate(Sum('suma'))
    args = {'suma_sum': suma_sum}

    return render(request, 'index.html', args)

def isllaidos(request):
    visi_laukai = Islaidos.objects.all()
    args = {'visi_laukai':visi_laukai}

    return render(request, 'islaidos.html', args)

def prideti(request):
    if request.method == 'GET':
        return render(request, 'prideti.html', {'form': Prideti()})
    else:
        try:
            form = Prideti(request.POST)
            naujas = form.save(commit=False)
            naujas.save()
            return redirect('index')
        except ValueError:
            return render(request, 'prideti.html', {'form': Prideti(), 'error': 'Bad data'})


def tipas(request):
    if request.method == 'GET':
        return render(request, 'tipas.html', {'form': PridetiTipa()})
    else:
        try:
            form = PridetiTipa(request.POST)
            naujas = form.save(commit=False)
            naujas.save()
            return redirect('index')
        except ValueError:
            return render(request, 'tipas.html', {'form': PridetiTipa(), 'error': 'Bad data'})