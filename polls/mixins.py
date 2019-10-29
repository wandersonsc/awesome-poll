from .models import Question


class QuestionMixins(object):

    model = Question
    context_object_name = 'questions'
