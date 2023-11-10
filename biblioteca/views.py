from django.shortcuts import render, redirect
from .models import Books, Genders
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='login')
def index(request):

    books = Books.objects.all()
    # for produto in produtos:
    #     print(f'produto.name + produto.price')

    return render(request, 'pages/index.html', {'books':books})

def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'pages/book_detail.html', {'book':book})