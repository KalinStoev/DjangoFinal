from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
# Create your views here.


class UserDetail(generic.DetailView, LoginRequiredMixin):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'register.html'

