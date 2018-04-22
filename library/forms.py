from django import forms
from .models import Book,Borrowing

class BookForm(forms.ModelForm):
    class Meta:
        
        model=Book
        fields=[
            'school',
            'book_number',
            'published_date',
            'Author',
            'book_title',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(  BookForm,self).__init__(*args,**kwargs)
         
    
class BorrowingForm(forms.ModelForm):
    class Meta:
        
        model=Borrowing
        fields=[
            'school',
            'book_number',
            'book_title',
            'student_number',
            'date_taken',
            'return_date',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(  BorrowingForm,self).__init__(*args,**kwargs)
         

                

