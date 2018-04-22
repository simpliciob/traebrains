from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
User=settings.AUTH_USER_MODEL
class Book(models.Model):
    user=models.ForeignKey(User)
    school=models.CharField(max_length=50)
    book_number=models.CharField(max_length=50,unique=True)
    published_date=models.DateField()
    Author=models.CharField(max_length=50)
    book_title=models.CharField(max_length=50)
    
    def __str__(self):
        return self.book_number
    def get_absolute_url(self):
        return reverse('library:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('library:updatebook', kwargs={'pk':self.pk})
class Borrowing(models.Model):
    school=models.CharField(max_length=50)
    user=models.ForeignKey(User)
    book_number=models.CharField(max_length=50,unique=True)
    book_title=models.CharField(max_length=50)
    student_number=models.CharField(max_length=50)
    
    date_taken=models.DateField()
    return_date=models.DateField()
    def __str__(self):
        return self.student_number
    def get_absolute_url(self):
        return reverse('library:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('library:update', kwargs={'pk':self.pk})


# Create your models here.
