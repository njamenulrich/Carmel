from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import UsersCreationForm
from users.models import Users

def home(request):
    return render(request, "home.html")

class SignUp(CreateView):
    form_class = UsersCreationForm
    success_url = reverse_lazy("login")
    template_name = "./registration/signup.html"
