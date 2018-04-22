from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FeesForm
from .models import Fee
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

class FeesListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return Fee.objects.filter(user=self.request.user)
    
 
    
class FeesDetailView(DetailView,LoginRequiredMixin):
    def get_queryset(self):
        return Fee.objects.filter(user=self.request.user)
    
    
class FeesCreateView(LoginRequiredMixin,CreateView):
    form_class=FeesForm
    login_url='/login/'
    template_name="fees/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return Fee.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(FeesCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Payment'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(FeesCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(FeesCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('fees:addfees')

    
    
class FeesUpdateView(LoginRequiredMixin,UpdateView):
    template_name="fees/update_fees.html"
    form_class=FeesForm
    def get_queryset(self):
        return Fee.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(FeesUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Fees'
        return context
    def get_form_kwargs(self):
        kwargs=super(FeesUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('fees:feeslist')
   



class FeesDeleteView(LoginRequiredMixin,DeleteView):
    model=  Fee
    template_name="fees/delete_fees.html"
    form_class=FeesForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(FeesDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        fee=Fee.objects.get(id=int(pk))
        context_data.update({'fee':fee})
        return context_data
    def get_success_url(self):
        return reverse('fees:feeslist')
   






# Create your views here.


# Create your views here.
