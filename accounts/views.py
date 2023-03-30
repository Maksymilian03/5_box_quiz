from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, FormView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
# Create your views here

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "__all__"
    redirect_authenticated_user = True


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('flashcards:flashcards')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *arg, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("flashcards:flashcards")
        return super(RegisterView, self).get(*arg, **kwargs)
    