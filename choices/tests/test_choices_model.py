
def test_choices_model(choice):

    assert choice.pk == 1


def test_string_representation(choice):

    assert str(choice) == choice.text
