from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookForm,BorrowingForm
from .models import Book,Borrowing
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View,DeleteView


class HomeView(View):
    def get(self,request,*args,**kwargs):
        #if not request.user.is_authenticated():
        return render(request, "exams/home.html",{})
        #user=request.user
        
        #is_following_user_ids=[x.user.id for x in user.is_following.all()]
        #qs=ExamMark.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        #for x in user.is_following.all():
            #return render(request, "teachers/home-feed.html",{"object_list":qs})

class BookListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    
        
    
class BorrowingListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return Borrowing.objects.filter(user=self.request.user)
   
 
    
class BookDetailView(DetailView,LoginRequiredMixin):
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    
    
class   BookCreateView(LoginRequiredMixin,CreateView):
    form_class=BookForm
    login_url='/login/'
    template_name="library/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(BookCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Book'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(BookCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(BookCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('library:addbook')

    
    
class BookUpdateView(LoginRequiredMixin,UpdateView):
    template_name="library/updatebook.html"
    form_class=BookForm
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(BookUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update book'
        return context
    def get_form_kwargs(self):
        kwargs=super(BookUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('library:booklist')
   

class BorrowingCreateView(LoginRequiredMixin,CreateView):
    form_class=BorrowingForm
    login_url='/login/'
    template_name="library/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return Borrowing.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(BorrowingCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add borrowing'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(BorrowingCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(BorrowingCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
class BorrowingUpdateView(LoginRequiredMixin,UpdateView):
    template_name="library/updateborrowing.html"
    form_class=BorrowingForm
    def get_queryset(self):
        return Borrowing.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(BorrowingUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update borrowing'
        return context
    def get_form_kwargs(self):
        kwargs=super(BorrowingUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('library:borrowlist')
   

class BookDeleteView(LoginRequiredMixin,DeleteView):
    model=  Book
    template_name="library/delete_book.html"
    form_class=BookForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(BookDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        book=Book.objects.get(id=int(pk))
        context_data.update({'book':book})
        return context_data
    def get_success_url(self):
        return reverse('library:booklist')
class BorrowingDeleteView(LoginRequiredMixin,DeleteView):
    model=  Borrowing
    template_name="library/delete_borrowing.html"
    form_class=BookForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(BorrowingDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        borrowing=Borrowing.objects.get(id=int(pk))
        context_data.update({'borrowing':borrowing})
        return context_data
    def get_success_url(self):
        return reverse('library:borrowinglist')
   






# Create your views here.


# Create your views here.


# Create your views here.
