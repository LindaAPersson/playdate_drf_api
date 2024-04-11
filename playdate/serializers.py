from rest_framework import serializers
from .models import Playdate

class PlaydateSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    is_organizer = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_organizer(self, obj):
        request = self.context['request']
        return request.user == obj.organizer

    class Meta:
        model = Playdate
        fields = [
            'id', 'title', 'image', 'date', 'location', 'description', 'organizer', 'prize', 'created_at', 'parent_stay_required', 'is_organizer'
        ]
