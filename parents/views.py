from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from exams.models import ExamMark
from coursework.models import Continuous_Assessment
from attendance.models import Attendance
from reports.models import Reports
from fees.models import Fee
from profiles.models import Profile
from library.models import Borrowing,Book
from hostels.models import Hostel
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View
from django.contrib.auth.models import User

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html",{})
        user=request.user
        
        is_following_user_ids=[x.user.id for x in user.is_following.all()]
        qs=Continuous_Assessment.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        for x in user.is_following.all():
            return render(request, "continuous/home-feed.html",{"object_list":qs})
    
    

#class Continuous_AssessmentListView(LoginRequiredMixin,ListView):
   
  # template_name="students/continuous_assessment_list.html"
   #model=Continuous_Assessment
   
   #def get_context_data(self,*args,**kwargs):
        #user=self.request.user
        
        #taken=super(Continuous_AssessmentListView, self).get_context_data(*args,**kwargs)
        #taken['locations'] =Continuous_Assessment.objects.filter(student_number=user)
        #return taken
class StudentListView(ListView,LoginRequiredMixin):
    template_name='parents/students_list.html'
    def get_queryset(self):
        return Profile.objects.filter(school=self.request.user).filter(is_student=True)
class TeacherListView(ListView,LoginRequiredMixin):
    template_name='parents/teachers_list.html'
    def get_queryset(self):
        return Profile.objects.filter(school=self.request.user).filter(is_teacher=True)
class FeeListView(ListView,LoginRequiredMixin):
    template_name='parents/fees_list.html'
    def get_queryset(self):
        return Fee.objects.filter(school=self.request.user)
class BookListView(ListView,LoginRequiredMixin):
    template_name='parents/bookis_list.html'
    def get_queryset(self):
        return Book.objects.filter(school=self.request.user)
class BorrowingListView(ListView,LoginRequiredMixin):
    template_name='parents/borrowings_list.html'
    def get_queryset(self):
        return Borrowing.objects.filter(school=self.request.user)  




# Create your views here.
