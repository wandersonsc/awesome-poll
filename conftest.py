import pytest
from mixer.backend.django import mixer


@pytest.fixture
def choice(db, question):

    choice = mixer.blend('choices.Choice', question=question, title='My Awesome Quiz')
    return choice


@pytest.fixture
def question(db):

    question = mixer.blend('polls.Question')
    return question
