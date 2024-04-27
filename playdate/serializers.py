from rest_framework import serializers
from .models import Playdate


class PlaydateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Playdate model.

    Attributes:
        organizer (ReadOnlyField): Username of the organizer of the playdate.
        is_organizer (SerializerMethodField): Indicates whether the current user is the organizer of the playdate.
        comments_count (ReadOnlyField): Total number of comments on the playdate.
        time (TimeField): Field representing the time of the playdate.
    
    Methods:
        validate_image: Validates the size and dimensions of the image uploaded for the playdate.
        get_is_organizer: Determines if the current user is the organizer of the playdate.
    """
    organizer = serializers.ReadOnlyField(source='organizer.username')
    is_organizer = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    time = serializers.TimeField(format='%H:%M')

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
            'id', 'title', 'image', 'date',
            'location', 'description', 'organizer',
            'prize', 'created_at', 'parent_stay_required',
            'is_organizer', 'comments_count', 'time', 'suitable_age'
        ]
