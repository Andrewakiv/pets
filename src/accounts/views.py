from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('pts:home')
    else:
        form = LoginForm()

    data = {
        'form': form
    }

    return render(request, 'accounts/login.html', context=data)


def logout(request):
    ...
