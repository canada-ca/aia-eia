# coding=utf-8

from django import template
from django.utils.translation import gettext


register = template.Library()


@register.filter('SwapLangCode', autoescape=True)
def other_lang_code(value):
    if str(value).lower() == 'en':
        return 'fr'
    elif str(value).lower() == 'fr':
        return 'en'
    else:
        return ''


@register.filter('SwapLangName', autoescape=True)
def other_lang(value):
    if str(value) == 'en':
        return 'Français'
    elif str(value) == 'fr':
        return 'English'
    else:
        return ''

@register.filter('EmptyFacetMessage', autoescape=True)
def search_facet_is_empty_message(value):
    msg = ''
    if type(value) is dict:
        c = 0
        for k,v in value.items():
            c = c + v
        if c == 0:
            msg = gettext("There are no filters for this search")
    return msg


@register.filter('ToMonth', autoescape=True)
def to_month(value):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    month_int = 0
    try:
        month_int = int(value)
    except ValueError:
        pass
    if month_int < 1 or month_int > 12:
        return ''
    else:
        return gettext(months[month_int - 1])




