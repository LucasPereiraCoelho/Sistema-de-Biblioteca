from django.shortcuts import render, redirect
from .models import Books, Genders, RentedBooks
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .app import send_email
from datetime import datetime
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

def user_logout(request):
    auth.logout(request)
    return redirect('login')

def search_book(request):
    q = request.GET.get('q')
    books = Books.objects.filter(name__icontains=q, in_stock=True)
    return render(request, 'pages/index.html', {'books':books})

def add_book(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        qtd_books = request.POST.get('qtd_books')
        qtd_pages = request.POST.get('qtd_pages')
        cover = request.FILES.get('cover')
        author = request.POST.get('author')
        in_stock = True
  
        Books.objects.create(
            name=name, 
            gender_id=gender, 
            qtd_books=qtd_books, 
            qtd_pages=qtd_pages,
            cover=cover, 
            author=author, 
            in_stock=in_stock
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
    RentedBooks.objects.create(
        user_id=request.user.id, 
        book_id=id
        )
    

    if book.qtd_books == 0:
        book.in_stock = False
    if book.qtd_books < 0:
        book.qtd_books = 0

    book.save()
    send_email(f"A Biblioteca do Senac informa, \nFoi confirmado seu emprestimo do livro {book.name} realizado no dia {datetime.now()}", request.user.email)
    return redirect ('book-detail', id)

def stockless(request):
    books = Books.objects.filter(in_stock=False)
    return render(request, 'pages/index.html', {'books':books})

def rented_books(request):
    livrosEmprestados = RentedBooks.objects.filter(user_id=request.user.id, returned=False)
    books = []
    for livroEmprestado in livrosEmprestados:
        books.append(livroEmprestado.book)
    
    return render(request, 'pages/rented_books.html', {'books': books})

def return_book(request, id):
    book = Books.objects.get(id=id)
    if not book.in_stock:
        book.in_stock = True
    book.qtd_books += 1
    book.save()

    rented_books = RentedBooks.objects.filter(book_id=id, user=request.user, returned=False)
    
    if rented_books.exists():
        rented_book = rented_books.first()
        rented_book.returned = True
        rented_book.save()
    
    return redirect('home')


    
