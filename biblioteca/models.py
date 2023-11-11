from django.db import models

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
    qtd_books = models.IntegerField() 
    qtd_pages = models.IntegerField()                              
    cover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    