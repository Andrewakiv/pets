from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.forms import LoginForm, RegisterForm, ProfileUserForm, UserChangePasswordForm


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return redirect('pts:home')
#     else:
#         form = LoginForm()
#
#     data = {
#         'form': form
#     }
#
#     return render(request, 'accounts/login.html', context=data)

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Authorization'}

    # def get_success_url(self):
    #     return reverse_lazy('pts:home')


# def logout_view(request):
#     logout(request)
#     return redirect('pts:home')
# can use class LogoutView instead of this func

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


class ProfileUser(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    template_name = 'accounts/profile.html'
    extra_context = {'title': 'Edit profile'}

    def get_success_url(self):
        return reverse_lazy('accounts:profile_view')

    def get_object(self, queryset=None):
        return self.request.user


class UserChangePassword(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done_view')
    # extra_context = {'title': 'Change password'}
