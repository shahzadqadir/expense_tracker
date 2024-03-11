from django.urls import path

from books import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("categories/", views.CategoryListView.as_view(), name="categories_list"),
]