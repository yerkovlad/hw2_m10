from django.urls import path
from .views import register, login_view, add_author, add_quote
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
    path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm')
]
