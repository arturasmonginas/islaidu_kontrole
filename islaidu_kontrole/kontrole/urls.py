from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('islaidos', views.isllaidos, name='islaidos'),
    path('prideti', views.prideti, name='prideti'),
    path('tipas', views.tipas, name='tipas')
]