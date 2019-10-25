
from django.urls import reverse


def test_polls_list_status_code(client):

    resp = client.get('/polls/')
    assert resp.status_code == 200


def test_view_url_by_name(client):

    url = reverse('polls:all')
    resp = client.get(url)
    assert resp.status_code == 200
