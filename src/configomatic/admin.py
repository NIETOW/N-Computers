from django.contrib import admin
from configomatic.models import Refroidissement, Boitier, Alimentation, SSD, MemoireVive, CarteMere, CarteGraphique, \
    Processeur


admin.site.register(Processeur)
admin.site.register(CarteGraphique)
admin.site.register(CarteMere)
admin.site.register(MemoireVive)
admin.site.register(SSD)
admin.site.register(Alimentation)
admin.site.register(Boitier)
admin.site.register(Refroidissement)

