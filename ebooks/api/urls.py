from django.urls import path, include
from . import views

urlpatterns = [
    path('ebooks/',
        views.EbookListCreateAPIView.as_view(),
        name='ebooks-list'),
    
    path('ebooks/<int:pk>/',
        views.EbookDetailAPIView.as_view(),
        name='ebooks-detail'),
    
    path('ebooks/<int:ebook_pk>/review/',
        views.ReviewCreateAPIView.as_view(),
        name='ebooks-review'),
    
    path('reviews/<int:pk>/',
        views.ReveiwDetailAPIView.as_view(),
        name='review-detail'),
    
    path('api-auth',
        include('rest_framework.urls'))
]