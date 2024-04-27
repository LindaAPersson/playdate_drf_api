from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer class to represent the current user.

    Attributes:
        user_id (ReadOnlyField): The read-only field representing the user's ID.
    """
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'user_id',
        )
        