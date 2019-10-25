from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Question


class PollListView(ListView):

    model = Question
    template_name = 'polls/polls_list.html'
    context_object_name = 'questions'


class PollDetailView(DetailView):

    model = Question
    template_name = 'polls/polls_detail.html'
    context_object_name = 'questions'
