from django.urls import reverse

from ..models import Question


def test_poll_detail_view(client):

    question = Question.objects.create(
        title='hello',
        slug='hello',
        approved_question=True
    )
    URL = reverse('polls:details',  kwargs={'slug': question.slug})
    resp = client.get(URL)
    assert resp.status_code == 200


def test_unapproved_question_fails(client):

    question = Question.objects.create(
        title='hello',
        slug='hello'
    )
    URL = reverse('polls:details',  kwargs={'slug': question.slug})
    resp = client.get(URL)
    assert resp.status_code == 404
