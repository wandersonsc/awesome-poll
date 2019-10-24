import pytest

from mixer.backend.django import mixer


@pytest.fixture
def question(db):
    question = mixer.blend('polls.Question')
    return question


def test_choices_model(db, question):

    choice = mixer.blend('choices.Choice', question=question, title='My Awesome Quiz')
    assert choice.pk == 1
    assert choice.title == 'My Awesome Quiz'
