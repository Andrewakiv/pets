from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from project import settings
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', views.login_view, name='login_view'),
    path('login/', views.LoginUser.as_view(), name='login_view'),
    # path('logout/', views.logout_view, name='logout_view'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout_view'),
    path('register/', views.register, name='register_view'),
    path('profile/', views.ProfileUser.as_view(), name='profile_view'),
    path('password-change/', views.UserChangePassword.as_view(), name='password_change_view'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done_view'),

    path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset_form.html',
                                                      email_template_name='accounts/password_reset_email.html',
                                                      success_url=reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html',
                                          success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
