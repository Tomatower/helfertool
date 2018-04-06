from django.db.models.functions import Lower
from django.db.models.query import QuerySet
from django.template import Library
from django.template.defaultfilters import stringfilter
from latex import escape

register = Library()

@register.filter
@stringfilter
def latex(value):
    try:
        return escape(value)
    except:
        return ''


@register.filter
def bykey(value, arg):
    try:
        return value[arg]
    except:
        return ''

@register.filter
def helpersort(value, arg):
    return value.extra(select={'case_insensitive_order': 'LOWER(' + arg + ')'})\
        .order_by('case_insensitive_order')
