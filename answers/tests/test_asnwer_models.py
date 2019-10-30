from mixer.backend.django import mixer


def test_answer_model(answer):

    assert answer.pk == 1


def test_string_representation(choice):

    answer = mixer.blend('answers.Answer', choice=choice)
    assert str(answer) == f'Choice {choice}'
