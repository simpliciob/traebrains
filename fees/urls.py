
from django.conf.urls import url,include
from .views import (FeesListView,
                    FeesCreateView,
                    FeesDetailView,
                    FeesUpdateView,
                    FeesDeleteView,
                    
                    )
    

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$',FeesDetailView.as_view(),name="fees-detail"),
    url(r'^list/$', FeesListView.as_view(),name="feeslist"),
    url(r'^create/$',FeesCreateView.as_view(),name="addfees"),
    url(r'^(?P<pk>[\w-]+)/update/$',FeesUpdateView.as_view(),name="update"),
    url(r'^(?P<pk>[\w-]+)/delete/$',FeesDeleteView.as_view(),name="delete-fee",)
    
    
    
]
