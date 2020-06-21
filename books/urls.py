# books/urls.py

from django.urls import path
from .views import BookListView, BookDetailView, SearchListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchListView.as_view(), name='search'),
]
