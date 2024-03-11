from django.urls import path

from books import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("categories/", views.CategoryListView.as_view(), name="categories_list"),
    path("books/", views.BookListView.as_view(), name="books_list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/update/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
]