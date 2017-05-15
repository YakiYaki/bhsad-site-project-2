from django import template
from facets.settings import STATIC_URL

register = template.Library()


@register.filter(name='get_icon')
def get_icon(num):
    return STATIC_URL + 'img/icon_small_' + str(num) + '.png'


@register.filter(name='get_label')
def get_label(data, i):
    print(data)
    return data[i]


@register.filter(name='get_data')
def get_data(obj):
    return obj.get_data()
