import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_hello_world(client):
    url = reverse('home')  # A URL de ViewsExercicio
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello World'  # Verifique o conteúdo exato


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('post_list')  # A URL de PostView
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello, World!'  # Verifique o conteúdo exato
