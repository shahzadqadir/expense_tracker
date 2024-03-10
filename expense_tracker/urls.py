from django.contrib import admin
from django.urls import path, include

from .views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("books.urls")),
    path("signup/", RegisterView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]
