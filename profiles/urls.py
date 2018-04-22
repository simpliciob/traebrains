
from .views import ProfileDetailView,ProfileListView,ProfileDeleteView,ProfileUpdateView,StudentListView

from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', ProfileListView.as_view(),name="profilelist"), 
    url(r'^(?P<pk>[\w-]+)/delete/$',ProfileDeleteView.as_view(),name="delete-user",),
    url(r'^(?P<pk>[\w-]+)/update/$',ProfileUpdateView.as_view(),name="update"),
    url(r'^student/$', StudentListView.as_view(),name="student"),
  

]
