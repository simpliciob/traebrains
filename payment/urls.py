
from django.conf.urls import url,include
from .views import (PaymentListView,
                    PaymentCreateView,
                    PaymentDetailView,
                    PaymentUpdateView,
                    PayementDeleteView,
                    
                    )
    

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$',PaymentDetailView.as_view(),name="fees-detail"),
    url(r'^list/$', PaymentListView.as_view(),name="feeslist"),
    url(r'^create/$',PaymentCreateView.as_view(),name="addfees"),
    url(r'^(?P<pk>[\w-]+)/update/$',PaymentUpdateView.as_view(),name="update"),
    url(r'^(?P<pk>[\w-]+)/delete/$',PaymentDeleteView.as_view(),name="delete-fee",)
    
    
    
]
