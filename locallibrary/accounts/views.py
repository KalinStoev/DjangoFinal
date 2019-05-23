from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
# Create your views here.


def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        redirect_url = f"{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=redirect_url)


def redirect_user(request):
    url = '/catalog/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView, LoginRequiredMixin):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'register.html'

