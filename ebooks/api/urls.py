from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/',
        views.EbookListCreateAPIView.as_view(),
        name='ebooks-list'),
    
    
]