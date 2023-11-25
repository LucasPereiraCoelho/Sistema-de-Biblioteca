from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from django.utils import timezone

class Genders(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
    

class Books(models.Model):

    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    qtd_books = models.IntegerField(default=0) 
    qtd_pages = models.IntegerField(default=0)                              
    cover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
class RentedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.book

    class Meta:
        verbose_name = 'RentedBook'
        verbose_name_plural = 'RentedsBooks'
