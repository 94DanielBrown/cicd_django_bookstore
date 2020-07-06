# books/views.py

from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Book
import logging
from django.conf import settings


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class SearchListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
