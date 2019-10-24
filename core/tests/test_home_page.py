import pytest

from django.test import Client
from django.urls import reverse

URL = reverse('home')


@pytest.fixture
def client(db):

    client = Client()
    return client


def test_home_page_status_code(client):

    resp = client.get('/')
    assert resp.status_code == 200


def test_view_url_by_name(client):

    resp = client.get(URL)
    assert resp.status_code == 200
