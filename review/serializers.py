from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.

    Attributes:
        user: A read-only field to represent the username of the user who made the review.
        is_user: A method field to check if the current user is the owner of the review.
        created_at: A method field to represent the creation time of the review in natural language.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'is_user',
            'created_at',
            'playdate_post',
            'comment',
            'attendance',
            'bring_this',
            'age_recommendation'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    playdate_post = serializers.ReadOnlyField(source='playdate_post.id')
