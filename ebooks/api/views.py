from rest_framework import generics
# from rest_framework import mixins
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from ebooks import models
from . import serializers
from . import permissions as custom_permissions
from . import paginations

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Ebook.objects.all()
    serializer_class = serializers.EbookSerializer
    permission_classes = [custom_permissions.IsAdminOrReadOnly,]
    pagination_class = paginations.SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ebook.objects.all()
    serializer_class = serializers.EbookSerializer
    permission_classes = [custom_permissions.IsAdminOrReadOnly,]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = generics.get_object_or_404(models.Ebook, pk=ebook_pk)

        review_author = self.request.user

        review_queryset = models.Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError({"error":"You have Already reviewed this ebook!!"})

        serializer.save(ebook=ebook, review_author=review_author)

class ReveiwDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [custom_permissions.IsAuthorReviewOrReadOnly,]

# class EbookListCreateAPIView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             generics.GenericAPIView):
    
#     queryset = models.Ebook.objects.all()
#     serializer_class = serializers.EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    