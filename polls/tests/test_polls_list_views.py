
from django.urls import reverse

URL = reverse('polls:all')


def test_polls_list_status_code(client):

    resp = client.get('/polls/')
    assert resp.status_code == 200


def test_view_url_by_name(client):

    resp = client.get(URL)
    assert resp.status_code == 200
