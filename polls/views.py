# from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render, Http404, HttpResponse

from .models import Question

from answers.models import Answer

from .mixins import QuestionMixins
from braces.views import SelectRelatedMixin, PrefetchRelatedMixin


class PollAllListView(SelectRelatedMixin, QuestionMixins, ListView):

    select_related = ['author']
    success_message = "Welcome!"
    template_name = 'polls/polls_list.html'


class PollDetailView(PrefetchRelatedMixin, SelectRelatedMixin, QuestionMixins, DetailView):

    prefetch_related = ['choices__answer_choices']
    select_related = ['author']
    template_name = 'polls/polls_detail.html'


# class PollListView(SelectRelatedMixin, QuestionMixins, CreateView):

#     select_related = ['author']
#     success_message = "Welcome!"
#     template_name = 'polls/polls_vote.html'
#     fields = ['name']


def vote(request, slug=None):

    if request.method == 'GET':
        try:
            question = Question.objects.get(slug=slug)
        except:
            raise Http404
        context = {}
        context['questions'] = question
        return render(request, 'polls/polls_vote.html', context)

    if request.method == 'POST':
        user_id = request.user.id
        print(f'My request: {request.POST}')
        data = request.POST
        selected_choice = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if selected_choice:
            return HttpResponse('Great! You Voted!')
        else:
            return HttpResponse('Fail!')
