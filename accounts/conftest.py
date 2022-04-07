import pytest
from django.contrib.auth.models import User

from autodetailing_app.models import About


@pytest.fixture
def user():
    return User.objects.create_user(username='carpro', password='showcar')


@pytest.fixture
def about():
    return About.objects.create(description='This is some text to check')