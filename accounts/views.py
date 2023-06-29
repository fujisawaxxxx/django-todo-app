from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    template_name="accounts/login.html"
    redirect_autheticated_user = True
    # ↑ログイン済みのユーザーにログイン画面を表示しない設定


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list') #どこのURLに飛ばすか