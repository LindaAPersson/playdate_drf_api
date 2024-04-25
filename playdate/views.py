from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Playdate
from .serializers import PlaydateSerializer
from .permissions import IsOwnerOrReadOnly
from datetime import date
from .filters import PlaydateFilter

# Create your views here.


class PlaydateList(generics.ListCreateAPIView):
    serializer_class = PlaydateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Playdate.objects.annotate(
            comments_count=Count('comment', distinct=True)
        )
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')
        if year and month:
            queryset = queryset.filter(date__year=year, date__month=month)

        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'organizer__username',
        'title',
        'location',
    ]
    ordering_fields = [
        'date',
    ]
    filterset_class = PlaydateFilter


class PlaydateListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaydateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Playdate.objects.all()
