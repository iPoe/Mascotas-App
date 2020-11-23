
from django import template

register = template.Library()
@register.simple_tag(takes_context=True)
def asignar_mascota(context, Mascota, *args, **kwargs):
    """
    Puts your variable into the main context under name ``my_node``.
    """
    context.dicts[0]['mascota_actual'] = Mascota
    print(Mascota.Nombre)
    return ''
