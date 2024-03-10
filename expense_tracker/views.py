from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrationForm

class RegisterView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")


