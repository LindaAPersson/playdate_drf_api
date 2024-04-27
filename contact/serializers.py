from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.

    Attributes:
        id (IntegerField): The unique identifier of the contact message.
        name (CharField): The name of the contact person.
        email (EmailField): The email address of the contact person.
        subject (CharField): The subject of the message.
        message (TextField): The content of the message.
        created_at (DateTimeField): The timestamp when the contact message was created.
    """
    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'email', 'subject', 'message', 'created_at',
        ]
