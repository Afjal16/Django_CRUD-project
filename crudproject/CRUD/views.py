from django.shortcuts import render,redirect
from .models import booklist

# Create your views here.

def index(request):
    books = booklist.objects.all()
    return render(request,'index.html',{'books':books })


def delete(request, id):
    books = booklist.objects.get(pk=id)
    books.delete()
    return redirect('/')


def edit(request, id):
    books = booklist.objects.get(pk=id)
    context = {
        'books':books
    }
    return render(request, 'edit.html', context)

def update(request, id):
    books = booklist.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')


def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = booklist(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')


def add_book(request):
    return render(request, 'add_book.html')

