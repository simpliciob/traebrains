
from django.conf.urls import url,include
from .views import (BookListView,
                    BorrowingListView,
                    BookCreateView,
                    BorrowingCreateView,
                    DetailView,
                    BorrowingUpdateView,
                    BorrowingDeleteView,
                    BookDeleteView,
                    BookUpdateView,
                    
                    )
    

urlpatterns = [
    
    
    url(r'^list/$', BookListView.as_view(),name="booklist"),
    url(r'^list/borrow/$', BorrowingListView.as_view(),name="borrowlist"),
    url(r'^create/book/$',BookCreateView.as_view(),name="addbook"),
    url(r'^(?P<pk>[\w-]+)/$',BookUpdateView.as_view(),name="updatebook"),
    url(r'^create/borrow/$',BorrowingCreateView.as_view(),name="addborrowing"),
    url(r'^(?P<pk>[\w-]+)/update/borrowing/$',BorrowingUpdateView.as_view(),name="updateborrow"),
    url(r'^(?P<pk>[\w-]+)/$',BookUpdateView.as_view(),name="updateborrowing"),
    url(r'^(?P<pk>[\w-]+)/update/book/$',BookUpdateView.as_view(),name="updatebook"),
    url(r'^(?P<pk>[\w-]+)/delete/book/$',BookDeleteView.as_view(),name="delete-book"),
    url(r'^(?P<pk>[\w-]+)/delete/borrowing/$',BorrowingDeleteView.as_view(),name="delete-borrow",)
    
    
    
]
