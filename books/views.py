from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Category, Book
from .forms import BookForm

# Create your views here.
def load_home(request):
    return render(
        request,
        'books/home.html'
    )


def list_books(request):
    books = Book.objects.all()
    if request.user.is_authenticated:
        return render(
            request, 
            'books/list_books.html',
            {'books': books}
        )
    else:
        return render(
            request,
            'books/home.html'
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
    if request.user.is_authenticated:
        return render(
            request,
            'books/view_book.html',
            {'book': book}
        )
    else:
        return render(
            request,
            'books/home.html'
        )


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else: 
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(
        request,
        'books/edit_book.html',
        {'form': form, 'book': book}
    )


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')

    return render(
        request,
        'books/delete_book.html',
        {'book': book}
    )


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.all()
    if request.user.is_authenticated:
        return render(
            request,
            'books/view_category.html',
            {'category': category, 'books': books}
        )
    else:
        return render(
            request,
            'books/home.html'
        )