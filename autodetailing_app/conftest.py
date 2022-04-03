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





# @pytest.fixture
# def author():
#     return Author.objects.create(first_name='slawek', last_name='bo')
#
#
# @pytest.fixture
# def books(author):
#     lst = []
#     for i in range(10):
#         x = Book.objects.create(
#             title=i,
#             year=i,
#             author=author
#         )
#         lst.append(x)
#     return lst