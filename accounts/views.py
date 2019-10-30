from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from . import forms


class SignUp(CreateView, SuccessMessageMixin):

    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    success_message = "Welcome, I hope you stick for the ride!"
