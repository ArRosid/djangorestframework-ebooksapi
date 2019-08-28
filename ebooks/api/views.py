from rest_framework import generics
from rest_framework import mixins

from ebooks import models
from . import serializers


class EbookListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    
    queryset = models.Ebook.objects.all()
    serializer_class = serializers.EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    