from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from books import models

class HomePageView(generic.TemplateView):

    template_name = "books/homepage.html"


class CategoryListView(generic.ListView):

    template_name = "books/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return models.Category.objects.all()
    

class BookListView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"

    paginate_by = 50    

    def get_queryset(self):
        return models.Book.objects.all()
    

class BookDetailView(generic.DetailView):
    template_name = "books/book_detail.html"
    context_object_name = "book"
    queryset = models.Book.objects.all()


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "books/book_update.html"
    context_object_name = "book"
    queryset = models.Book.objects.all()
    
    def get_success_url(self, **kwargs) -> str:
        return reverse("book_detail", kwargs={"pk": self.object.id})

    fields = (
        "serial",
        "title",
        "subtitle",
        "authors",
        "publisher",
        "published_date",
        "category",
        "distribution_expense",
    )


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "books/book_delete.html"
    context_object_name = "book"
    queryset = models.Book.objects.all()

    success_url = reverse_lazy("books_list")
