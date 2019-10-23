from mixer.backend.django import mixer


def test_poll_models(db):

    poll = mixer.blend('polls.Question')
    assert poll.pk == 1
