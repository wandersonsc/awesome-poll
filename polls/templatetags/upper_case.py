from django import template

from ..models import Question

register = template.Library()


@register.filter
def upper_case(value):

    return value.upper()
