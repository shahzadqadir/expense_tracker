from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db.models import ProtectedError

from books import models
from books import forms

class HomePageView(generic.TemplateView):
    template_name = "books/homepage.html"


class CategoryListView(generic.ListView):

    template_name = "books/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return models.Category.objects.all()
    

class CategoryCreateView(generic.CreateView):

    template_name = "books/category_create.html"
    context_object_name = "category"
    queryset = models.Category.objects.all()
    success_url = reverse_lazy("categories_list")

    fields = {
        "name",
    }
    

class CategoryUpdateView(generic.UpdateView):
    template_name = "books/category_update.html"
    context_object_name = "category"
    queryset = models.Category.objects.all()
    success_url = reverse_lazy("categories_list")

    fields = (
        "name",
    )


class CategoryDeleteView(generic.DeleteView):
    template_name = "books/category_delete.html"
    context_object_name = "category"
    queryset = models.Category.objects.all()
    success_url = reverse_lazy("categories_list")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Can't delete category without deleting all books in this category!")
        finally:
            return redirect(self.success_url)

class BookListView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"

    paginate_by = 50    

    def get_queryset(self):
        return models.Book.objects.all()
    
    def get_context_data(self, **kwargs):
        form = forms.BookSearchForm()
        context = super(BookListView, self).get_context_data(**kwargs)
        context["form"] = form
        return context
    
    def post(self, request, *args, **kwargs):
        term = request.POST.get("q")
        books = self.get_queryset().filter(title__icontains=term)        
        return render(request, self.template_name, {"books": books, "books_found": len(books)})


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


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "books/book_create.html"
    queryset = models.Book.objects.all()
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
    success_url = reverse_lazy("books_list")

# def book_search(request):
#     form = forms.BookSearch()
#     books = models.Book.objects.all()
#     if request.method == "POST":
#         pass
#     return render(request, "books/books_list.html", {"books": books})