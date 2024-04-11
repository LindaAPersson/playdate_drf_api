from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'is_user', 'created_at', 'playdate_post', 'content'
        ]   

class CommentDetailSerializer(CommentSerializer):
    
    playdate_post = serializers.ReadOnlyField(source='playdate_post.id')

