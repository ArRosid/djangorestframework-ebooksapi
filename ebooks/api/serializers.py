from rest_framework import serializers
from ebooks import models

class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = models.Review
        fields = "__all__"

class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = models.Ebook
        fields = "__all__"

