def test_poll_models(question):

    assert question.pk == 1


def test_string_representation(question):

    assert str(question) == question.title
