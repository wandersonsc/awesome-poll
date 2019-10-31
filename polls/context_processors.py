from .models import Question


def polls_count(request):

    count = Question.objects.filter(approved_question=True).count()
    return {'polls_count': count}
