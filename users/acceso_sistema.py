# user views
# Django
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import login, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.template import Context
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Django decorators
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

#Form
from users.forms import SignupForm, LoginForm 

class SignupView(FormView):
    # Signup con classe base view
    template_name='users/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('users:validate_token')

    def form_valid(self, form):
        # save form data
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(email=email, password=password)
            login(self.request, user)
            return super().form_valid(form)

class LoginView(FormView):
    # login view
    template_name='users/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('posts:feed')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass