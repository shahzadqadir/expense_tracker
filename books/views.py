from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views import generic
from books import models

class HomePageView(generic.TemplateView):

    template_name = "books/homepage.html"


class CategoryListView(generic.ListView):

    template_name = "books/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return models.Category.objects.all()