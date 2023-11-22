from django.shortcuts import render


def produits(request):
    return render(request, 'djangotests/produits.html')


def accueil(request):
    return render(request, "djangotests/index.html")
