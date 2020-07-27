from django.contrib import admin
from .models import Islaidu_tipai, Islaidos

class IslaiduAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'aktyvus',)

class IslaidosAdmin(admin.ModelAdmin):
    list_display = ('data', 'tipas', 'tiekejas', 'dokumento_nr', 'suma')

admin.site.register(Islaidos, IslaidosAdmin)
admin.site.register(Islaidu_tipai, IslaiduAdmin)
