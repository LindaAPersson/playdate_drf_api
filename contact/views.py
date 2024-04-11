from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.

class AdminCanReadContactPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class ContactList(generics.ListCreateAPIView):
    
    serializer_class = ContactSerializer
    permission_classes = [AdminCanReadContactPermission]
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
    
    serializer_class = ContactSerializer
    permission_classes = [AdminCanReadContactPermission]
    queryset = Contact.objects.all()