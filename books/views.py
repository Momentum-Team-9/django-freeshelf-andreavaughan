from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Category, Book

# Create your views here.
def load_home(request):
    return render(
        request,
        'base.html'
    )


def list_books(request):
    books = Book.objects.all()
    return render(
        request, 
        'books/list_books.html',
        {'books': books}
    )