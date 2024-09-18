from django import template
from recipes.utils import choose_plural

register = template.Library()


@register.filter
def choose_plural_word(value):
    result = choose_plural(int(value), ('человек', 'человек', 'человек'))
    return result[1]


@register.filter
def calculate(value, count):
    return round(value * int(count), 2)