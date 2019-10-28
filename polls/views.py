# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView


from .mixins import QuestionMixinx
from braces.views import SelectRelatedMixin, PrefetchRelatedMixin


class PollListView(SelectRelatedMixin, QuestionMixinx, ListView):

    select_related = ['author']
    success_message = "Welcome!"
    template_name = 'polls/polls_list.html'


class PollDetailView(PrefetchRelatedMixin, SelectRelatedMixin, QuestionMixinx, DetailView):

    prefetch_related = ['choices__answer_choices']
    select_related = ['author']
    template_name = 'polls/polls_detail.html'
