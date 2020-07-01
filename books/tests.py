# books/tests.py
from django.urls import reverse
import pytest
from django.contrib.auth import get_user_model
from .models import Book, Review


# Tests for book
@pytest.fixture(scope='module')
def book(django_db_setup, django_db_blocker):
    print('setup')
    with django_db_blocker.unblock():
        # Create user to be used for test review
        user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
    # Create test book in database
        book = Book.objects.create(
            title='Django for professionals',
            author='William S. Vincent',
            price='30.00',
        )
    # Create test review in database
        review = Review.objects.create(
            book=book,
            author=user,
            review='Terrific review',
        )
    return book


# book = Book.objects.get(title='Django for professionals')
@pytest.mark.django_db
def test_create_book(book, client):
    assert book.title == 'Django for professionals'
    assert book.author == 'William S. Vincent'
    assert book.price == '30.00'


@pytest.mark.django_db
def test_book_list_view(book, client):
    response = client.get(reverse('book_list'))
    assert response.status_code == 200
    assert 'Django for professionals' in str(response.content)


@pytest.mark.django_db
def test_book_detail_view(book, client):
    response = client.get(book.get_absolute_url())
    no_response = client.get('/books/12345')
    assert response.status_code == 200
    assert no_response.status_code == 404
    # Test review
    assert 'Terrific review' in str(response.content)
