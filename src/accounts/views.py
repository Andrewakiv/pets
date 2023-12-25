from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.forms import LoginForm


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
