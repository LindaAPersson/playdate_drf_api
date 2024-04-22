from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Playdate
from .serializers import PlaydateSerializer
from .permissions import IsOwnerOrReadOnly
from datetime import date

# Create your views here.

class PlaydateList(generics.ListCreateAPIView):
    
    serializer_class = PlaydateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Playdate.objects.annotate(
        comments_count=Count('comment', distinct=True)
        )
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            queryset = queryset.filter(date__lte=end_date)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'organizer',
        'title',
        'location',
        'parent_stay_required',
        'suitable_age'
    ]
    search_fields = [
        'organizer__username',
        'title',
        'location',
    ]
    ordering_fields = [
        'date',
    ]

class PlaydateListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaydateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Playdate.objects.all()

    