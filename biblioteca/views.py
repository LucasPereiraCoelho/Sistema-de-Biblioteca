from django.shortcuts import render, redirect
from .models import Books, Genders
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='login')
def index(request):

    books = Books.objects.filter(in_stock=True)
    # for produto in produtos:
    #     print(f'produto.name + produto.price')

    return render(request, 'pages/index.html', {'books':books})

def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'pages/book_detail.html', {'book':book})

def add_book(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        qtd_books = request.FILES.get('qtd_books')
        qtd_pages = request.FILES.get('qtd_pages')
        cover = request.POST.get('cover')
        author = request.POST.get('author')
        in_stock = True
  
        Books.objects.create(
            name=name, gender_id=gender, qtd_books=qtd_books, qtd_pages=qtd_pages,
            cover=cover, author=author, in_stock=in_stock
        )

        return redirect('home')

    else:
        genders = Genders.objects.all()
        return render(request, 'pages/add_book.html', {'genders':genders}) 

def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect ('home')

def rent_book(request, id):
    book = Books.objects.get(id=id)
    book.qtd_books -= 1
    if book.qtd_books == 0:
        book.in_stock = False
    if book.qtd_books < 0:
        book.qtd_books = 0
    book.save()
    return redirect ('book-detail', id)

def stockless():
    books = Books.objects.filter(in_stock=False)
    return render(request, 'pages/index.html', {'books':books})