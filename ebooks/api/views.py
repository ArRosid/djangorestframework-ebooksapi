from rest_framework import generics
# from rest_framework import mixins
from rest_framework import permissions

from ebooks import models
from . import serializers
from . import permissions as custom_permissions

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Ebook.objects.all()
    serializer_class = serializers.EbookSerializer
    permission_classes = [custom_permissions.IsAdminOrReadOnly,]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ebook.objects.all()
    serializer_class = serializers.EbookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = generics.get_object_or_404(models.Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)

class ReveiwDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


# class EbookListCreateAPIView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             generics.GenericAPIView):
    
#     queryset = models.Ebook.objects.all()
#     serializer_class = serializers.EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    