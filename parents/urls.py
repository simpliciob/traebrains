
from .views import StudentListView,TeacherListView,BookListView,BorrowingListView,FeeListView

from django.conf.urls import url

urlpatterns = [
    url(r'^student/$', StudentListView.as_view(),name="student"),
    url(r'^teacher/$', TeacherListView.as_view(),name="teacher"),
    url(r'^payment/$', FeeListView.as_view(),name="payment"),
    url(r'^books/$', BookListView.as_view(),name="books"),
    url(r'^borrowings/$', BorrowingListView.as_view(),name="borrowing"), 

]
