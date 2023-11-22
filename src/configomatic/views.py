from django.shortcuts import render
from configomatic.models import Processeur, CarteGraphique, Boitier, Alimentation, DisqueDur, SSD, MemoireVive, CarteMere, \
    Refroidissement


def configomatic(request):
    processeurs = Processeur.objects.all()
    cartes_meres = CarteMere.objects.all()
    memoires_vives = MemoireVive.objects.all()
    ssd = SSD.objects.all()
    disques_durs = DisqueDur.objects.all()
    alimentations = Alimentation.objects.all()
    boitiers = Boitier.objects.all()
    refroidissements = Refroidissement.objects.all()
    cartes_graphiques = CarteGraphique.objects.all()

    carte_mere_selectionnee = request.GET.get('carte_mere')

    print(carte_mere_selectionnee)
    carte_mere_selectionnee = request.GET.get('carte_mere')

    if carte_mere_selectionnee:
        memoires_vives = memoires_vives.filter(typeRAM='DDR5', carte_mere__id=carte_mere_selectionnee)

    return render(request, 'configomatic/configomatic.html', context={
        'processeurs': processeurs,
        'cartes_graphiques': cartes_graphiques,
        'cartes_meres': cartes_meres,
        'memoires_vives': memoires_vives,
        'ssd': ssd,
        'disques_durs': disques_durs,
        'alimentations': alimentations,
        'boitiers': boitiers,
        'refroidissements': refroidissements,
        'carte_mere_selectionnee': carte_mere_selectionnee,  # Ajout de la variable carte_mere_selectionnee au contexte
    })