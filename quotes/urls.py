from django.urls import path
from .views import register, login_view, add_author, add_quote

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
]
