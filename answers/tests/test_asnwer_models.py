def test_answer_model(answer):

    assert answer.pk == 1


def test_string_representation(answer):

    assert str(answer) == answer.answer
