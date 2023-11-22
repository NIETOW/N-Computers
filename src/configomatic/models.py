from django.db import models


class Processeur(models.Model):
    name = models.CharField(max_length=128)
    socket = models.CharField(max_length=128, blank=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    consommation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class CarteGraphique(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    consommation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class CarteMere(models.Model):
    DDR3 = 'DDR3'
    DDR4 = 'DDR4'
    DDR5 = 'DDR5'

    RAM_CHOICES = (
        (DDR3, 'DDR3'),
        (DDR4, 'DDR4'),
        (DDR5, 'DDR5'),
    )

    name = models.CharField(max_length=128)
    socket = models.CharField(max_length=128, blank=True)
    typeRAM = models.CharField(max_length=128, choices=RAM_CHOICES, blank=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    m2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class MemoireVive(models.Model):
    DDR3 = 'DDR3'
    DDR4 = 'DDR4'
    DDR5 = 'DDR5'

    RAM_CHOICES = (
        (DDR3, 'DDR3'),
        (DDR4, 'DDR4'),
        (DDR5, 'DDR5'),
    )

    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    typeRAM = models.CharField(max_length=128, choices=RAM_CHOICES, blank=True)

    carte_mere = models.ForeignKey(CarteMere, on_delete=models.CASCADE, related_name='memoires_vives',
                                   default=1)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class SSD(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    m2 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class DisqueDur(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class Alimentation(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    puissance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class Boitier(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"


class Refroidissement(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"