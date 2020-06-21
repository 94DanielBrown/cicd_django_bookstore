from django.contrib.auth import get_user_model
from django.urls import reverse  # , resolve
import pytest
# from .views import SignUpPageView


# from . import forms


# User creation tests
@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        username='will',
        email='will@email.com',
        password='testpass123'
    )
    assert user.username == 'will'
    assert user.email == 'will@email.com'
    assert user.is_active
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_super_user():
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@email.com',
        password='testpass123'
    )
    assert admin_user.username == 'superadmin'
    assert admin_user.email == 'superadmin@email.com'
    assert admin_user.is_active
    assert admin_user.is_superuser


# Sign Up tests
@pytest.fixture
def response(client):
    url = reverse('account_signup')
    response = client.get(url)
    return response


def test_signup_template(response):
    assert response.status_code == 200
    assert 'account/signup.html' in (t.name for t in response.templates)
    assert 'Sign Up' in str(response.content)
    assert 'Some silly string' not in str(response.content)


""" NOT REQUIRED WITH allauth as uses it's own view and form
@pytest.mark.django_db
def test_signup_form():
    data = {'email': 'bgates@microsoft.com', 'username': 'bgates',
            'password1': 'randomstring456', 'password2': 'randomstring456'}
    Form = forms.CustomUserCreationForm(data=data)
    assert Form.is_valid() is True


def test_signup_view(client):
    response = resolve('/accounts/signup/')
    assert response.func.__name__ == SignUpPageView.as_view().__name__
    """
