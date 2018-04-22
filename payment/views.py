from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PaymentForm
from .models import Payment
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

class PaymentListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(PaymentListView, self).get_context_data(*args,**kwargs)
        query=self.request.GET.get('q')
        qs=Payment.objects.filter(user=self.request.user).search(query)
    
        
            
        if qs.exists():
            context['locations']=qs
        
        return context
 
    
class PaymentDetailView(DetailView,LoginRequiredMixin):
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
    
    
class PaymentCreateView(LoginRequiredMixin,CreateView):
    form_class=FeeForm
    login_url='/login/'
    template_name="payment/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(PaymentCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Payment'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(PaymentCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(PaymentCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('payment:addfees')

    
    
class PaymentUpdateView(LoginRequiredMixin,UpdateView):
    template_name="payment/update_fees.html"
    form_class=PaymentForm
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(PaymentUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Fees'
        return context
    def get_form_kwargs(self):
        kwargs=super(PaymentUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('payment:feeslist')
   



class PaymentDeleteView(LoginRequiredMixin,DeleteView):
    model=Payment
    template_name="payment/delete_fees.html"
    form_class=FeesForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(paymentDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        payment=Payment.objects.get(id=int(pk))
        context_data.update({'payment':payment})
        return context_data
    def get_success_url(self):
        return reverse('payment:feeslist')
   






# Create your views here.


# Create your views here.
