
from django.conf.urls import url,include
from .views import (HostelListView,
                    HostelCreateView,
                    HostelDetailView,
                    HostelUpdateView,
                    HostelDeleteView,
                    
                    )
    

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$',HostelDetailView.as_view(),name="hostel-detail"),
    url(r'^list/$', HostelListView.as_view(),name="hostellist"),
    url(r'^create/$',HostelCreateView.as_view(),name="addhostel"),
    url(r'^(?P<pk>[\w-]+)/$',HostelUpdateView.as_view(),name="updatem"),
    url(r'^(?P<pk>[\w-]+)/update/$',HostelUpdateView.as_view(),name="update-hostel"),
    url(r'^(?P<pk>[\w-]+)/delete/$',HostelDeleteView.as_view(),name="delete-hostel",)
    
    
    
]
