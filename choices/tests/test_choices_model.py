
def test_choices_model(choice):

    assert choice.pk == 1
    assert choice.title == 'My Awesome Quiz'


def test_string_representation(choice):

    assert str(choice) == choice.title
