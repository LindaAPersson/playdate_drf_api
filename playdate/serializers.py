from rest_framework import serializers
from .models import Playdate

class PlaydateSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='user')

    class Meta:
        model = Playdate
        fields = [
            'id', 'title', 'image', 'date', 'location', 'description', 'organizer', 'prize', 'created_at', 'parent_stay_required'
        ]
