from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HostelForm
from .models import Hostel
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

class HostelListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return Hostel.objects.filter(user=self.request.user)
    
 
    
class HostelDetailView(DetailView,LoginRequiredMixin):
    def get_queryset(self):
        return Hostel.objects.filter(user=self.request.user)
    
    
class HostelCreateView(LoginRequiredMixin,CreateView):
    form_class=HostelForm
    login_url='/login/'
    template_name="hostels/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return Hostel.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(HostelCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Accomodation'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(HostelCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(HostelCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('hostels:addhostel')

    
    
class HostelUpdateView(LoginRequiredMixin,UpdateView):
    template_name="hostels/update_hostel.html"
    form_class=HostelForm
    def get_queryset(self):
        return Hostel.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(HostelUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update hostel'
        return context
    def get_form_kwargs(self):
        kwargs=super(HostelUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('hostel:hostellist')
   



class HostelDeleteView(LoginRequiredMixin,DeleteView):
    model=Hostel
    template_name="hostels/delete_hostel.html"
    form_class=HostelForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(HostelDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        hostel=Fee.objects.get(id=int(pk))
        context_data.update({'hostel':hostel})
        return context_data
    def get_success_url(self):
        return reverse('hostel:hostellist')
   






# Create your views here.


# Create your views here.
