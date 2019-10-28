from .models import Question


class QuestionMixinx(object):

    model = Question
    context_object_name = 'questions'
