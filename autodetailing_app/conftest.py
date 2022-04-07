import pytest
from django.contrib.auth.models import User

from autodetailing_app.models import Service, Category, Worker, Order, Cart, Opinion, About


@pytest.fixture
def about():
    return About.objects.create(description='This is some text to check')


@pytest.fixture
def category():
    return Category.objects.create(name='example', description='Text to check')


@pytest.fixture
def category_id_2():
    return Category.objects.create(pk=2)


@pytest.fixture
def user():
    return User.objects.create_user(username='carpro', password='showcar')


@pytest.fixture
def some_id():
    for i in range(1, 3):
        return str(i)


@pytest.fixture
def service(some_id):
    return Service.objects.create(pk=some_id)


@pytest.fixture
def cart(user):
    return Cart.objects.create(user=user)


@pytest.fixture
def is_done():
    return True


@pytest.fixture
def worker(some_id):
    return Worker.objects.create(pk=some_id)


@pytest.fixture
def order(some_id):
    return Order.objects.create(pk=some_id)
