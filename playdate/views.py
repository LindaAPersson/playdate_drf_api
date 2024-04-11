from rest_framework import generics, permissions
from .models import Playdate
from .serializers import PlaydateSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class PlaydateList(generics.ListCreateAPIView):
    
    serializer_class = PlaydateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Playdate.objects.all()

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class PlaydateListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaydateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Playdate.objects.all()

    