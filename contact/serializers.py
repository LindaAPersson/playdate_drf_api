from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'email', 'subject', 'message', 'created_at',
        ] 