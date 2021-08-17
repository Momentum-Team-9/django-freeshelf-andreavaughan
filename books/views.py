from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Category, Book
from .forms import BookForm

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


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else: 
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(
        request,
        'books/add_book.html',
        {'form': form}
    )


def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(
        request,
        'books/view_book.html',
        {'book': book}
    )


def edit_book(request, pk):
    pass


def delete_book(request, pk):
    pass