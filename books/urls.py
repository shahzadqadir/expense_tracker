from django.urls import path

from books import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("categories/", views.CategoryListView.as_view(), name="categories_list"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/update/", views.CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", views.CategoryDeleteView.as_view(), name="category_delete"),
    path("books/", views.BookListView.as_view(), name="books_list"),
    path("books/create/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/update/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
]