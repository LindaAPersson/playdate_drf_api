from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.


class ContactList(generics.ListCreateAPIView):
    """
    Views for handling contact messages.

    Examples:
        ContactList: Handles listing and creating contact messages.
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'name',
    ]

    def perform_create(self, serializer):
        serializer.save()


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Views for handling contact messages.

    Examples:
        ContactDetail: Handles retrieving, updating, or deleting a specific contact message.
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
