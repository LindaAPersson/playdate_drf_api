from rest_framework import serializers
from .models import Playdate

class PlaydateSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    is_organizer = serializers.SerializerMethodField()

    def get_is_organizer(self, obj):
        request = self.context['request']
        return request.user == obj.organizer

    class Meta:
        model = Playdate
        fields = [
            'id', 'title', 'image', 'date', 'location', 'description', 'organizer', 'prize', 'created_at', 'parent_stay_required', 'is_organizer'
        ]
