from django import template
from theme.models import CarteMere

register = template.Library()


@register.filter
def is_compatible_with_carte_mere(memoire_vive, carte_mere_id):
    carte_mere = CarteMere.objects.get(id=carte_mere_id)
    return memoire_vive.typeRAM == carte_mere.typeRAM
