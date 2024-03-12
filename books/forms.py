from django import forms

from books import models

class CategoryForm(forms.ModelForm):
    model = models.Category
    fields = ["name, "]


class BookForm(forms.ModelForm):
    model = models.Book
    fields = [
        "id",
        "title",
        "subtitle",
        "authors",
        "publisher",
        "published_date",
        "category",
        "distribution_expense",
    ]


class BookSearchForm(forms.Form):
    search = forms.CharField(max_length=255,
                             widget=forms.TextInput
                             (attrs={"placeholder": "Search a book", "name": "q"}),
                             label="")