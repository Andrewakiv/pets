from django.contrib.auth.views import LogoutView
from django.urls import path

from project import settings
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', views.login_view, name='login_view'),
    path('login/', views.LoginUser.as_view(), name='login_view'),
    # path('logout/', views.logout_view, name='logout_view'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout_view'),
]
