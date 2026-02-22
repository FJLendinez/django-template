from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .views import login_view, user_settings, change_password

app_name = 'users'

urlpatterns = [
    path("login/", login_view, name='login'),
    path("logout/", auth_views.logout_then_login, name='logout'),
    path("user/settings/", user_settings, name='user_settings'),
    path("user/change_password/", change_password, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
