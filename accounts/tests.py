from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
import pytest

from django.urls import reverse

from accounts.forms import LoginForm, RegisterForm


@pytest.mark.django_db
def test_login_view_get():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], LoginForm)


@pytest.mark.django_db
def test_login_view_post(user, about):
    client = Client()
    data = {
        'username': 'carpro',
        'password': 'showcar'
    }
    url = reverse('login')
    response = client.post(url, data)
    assert response.wsgi_request.user.is_authenticated
    client.force_login(user)
    new_url = reverse('main')
    response = client.get(new_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_view(user, about):
    client = Client()
    url = reverse('logout')
    client.logout()
    response = client.get(url)
    assert response.status_code == 302
    new_url = reverse('main')
    response = client.get(new_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_view_get():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], RegisterForm)


@pytest.mark.django_db
def test_register_view_post():
    client = Client()
    data = {
        'username': 'carpro',
        'password': 'showcar',
        'email': 'carpro@car.eu'
    }
    url = reverse('register')
    response = client.post(url, data)
    assert User.objects.count() == 1
    assert response.status_code == 302
    new_url = reverse('login')
    response = client.post(new_url)
    assert response.status_code == 200
