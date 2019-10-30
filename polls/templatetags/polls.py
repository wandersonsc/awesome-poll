from django import template

from ..models import Question

register = template.Library()


@register.simple_tag
def show_poll():

    polls = Question.objects.count()
    print(f'MY POLLS: {polls}')
    return polls
