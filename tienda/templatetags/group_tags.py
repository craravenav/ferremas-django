from django import template

register = template.Library()

@register.filter(name='es_Vendedor')
def es_Vendedor(user):
    return user.groups.filter(name='Vendedor').exists()

@register.filter(name='es_Contador')
def es_Contador(user):
    return user.groups.filter(name='Contador').exists()