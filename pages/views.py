# pages/views
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PermissionsTestView(LoginRequiredMixin, TemplateView):
    template_name = 'permissions_test.html'
    login_url = 'account_login'
