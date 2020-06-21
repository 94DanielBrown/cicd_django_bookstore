# pages/tests
import pytest
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

# Homepage Tests


@pytest.fixture
def home_response(client):
    home_response = client.get(reverse('home'))
    return home_response


def test_homepage_status_code(home_response):
    assert home_response.status_code == 200


def test_homepage_url_name(home_response):
    assert home_response.status_code == 200


def test_homepage_template(home_response):
    assert 'home.html' in (t.name for t in home_response.templates)


def test_homepage_contains_correct_html(home_response):
    assert 'Homepage' in str(home_response.content)


def test_homepage_does_not_contain_incorrect_html(home_response):
    assert 'Some silly sentence' not in str(home_response.content)


def test_homepage_url_resolves_homepageview():
    view = resolve('/')
    assert view.func.__name__ == HomePageView.as_view().__name__


# About page tests


@pytest.fixture
def about_response(client):
    about_response = client.get(reverse('about'))
    return about_response


def test_about_status_code(about_response):
    assert about_response.status_code == 200


def test_about_url_name(about_response):
    assert about_response.status_code == 200


def test_about_template(about_response):
    assert 'about.html' in (t.name for t in about_response.templates)


def test_aboutpage_contains_correct_html(about_response):
    assert 'About' in str(about_response.content)


def test_aboutpage_does_not_contain_incorrect_html(about_response):
    assert 'Some silly sentence' not in str(about_response.content)


def test_aboutpage_url_resolves_aboutpageview():
    view = resolve('/about/')
    assert view.func.__name__ == AboutPageView.as_view().__name__
