"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from books import views as books_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', books_views.load_home, name='home'), 
    path('books', books_views.list_books, name='list_books'),
    path('books/add', books_views.add_book, name='add_book'),
    path('books/<int:pk>', books_views.view_book, name='view_book'),
    path('books/<int:pk>/edit', books_views.edit_book, name='edit_book'), 
    path('books/<int:pk>/delete', books_views.delete_book, name='delete_book'),
    path('categories/<slug:slug>', books_views.view_category, name='view_category'),
    path('books/favorites', books_views.view_favorites, name='view_favorites'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns