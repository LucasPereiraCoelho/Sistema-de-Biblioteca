from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book-detail/<int:id>/', views.book_detail, name='book-detail'),
    path('delete-book/<int:id>/', views.delete_book, name='delete-book'),
    path('rent-book/<int:id>/', views.rent_book, name='rent-book'),
    path('stockless/', views.stockless, name='stockless'),
    path('add-book/', views.add_book, name='add-book')


]