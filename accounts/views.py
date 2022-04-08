from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from accounts.forms import LoginForm, RegisterForm, UpdateUserPermissionForm
from autodetailing_app.models import Cart


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'autodetailing_app/login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                user = request.user
                if hasattr(user, 'cart'):
                    cart = user.cart
                else:
                    cart = Cart.objects.create(user=user)
                redirect_url = request.GET.get('next', 'main')
                return redirect(redirect_url)
        message = "Podany login lub hasło jest nieprawidłowe !"
        return render(request, 'autodetailing_app/login_form.html', {'form': form, 'message': message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'autodetailing_app/register_form.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
        return render(request, 'autodetailing_app/register_form.html', {'form': form})


class UserPermissionUpdateView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UpdateUserPermissionForm(instance=user)
        return render(request, 'autodetailing_app/permission_form.html', {'form': form})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UpdateUserPermissionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'autodetailing_app/permission_form.html', {'form': form})


class AllAccountsView(View):
    def get(self, request):
        users = User.objects.all().order_by('id')
        return render(request, 'autodetailing_app/all_users.html', {'users': users})
