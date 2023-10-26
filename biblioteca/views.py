from django.shortcuts import render, redirect
from .models import Books, Genders

# Create your views here.


def index(request):

    books = Books.objects.all()
    # for produto in produtos:
    #     print(f'produto.name + produto.price')

    return render(request, 'pages/index.html', {'books':books})