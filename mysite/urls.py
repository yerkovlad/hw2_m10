from django.contrib import admin
from django.urls import path, include
from quotes.views import index, add_author, add_quote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
    path('accounts/', include('django.contrib.auth.urls')),
]