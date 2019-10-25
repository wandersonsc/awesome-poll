import pytest
from django.test import Client

from mixer.backend.django import mixer


@pytest.fixture
def choice(db, question):

    choice = mixer.blend('choices.Choice', question=question, title='My Awesome Quiz')
    return choice


@pytest.fixture
def client(db):

    client = Client()
    return client


@pytest.fixture
def question(db):

    question = mixer.blend('polls.Question')
    return question


@pytest.fixture
def answer(db):

    answer = mixer.blend('answers.Answer')
    return answer
