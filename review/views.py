from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer

# Create your views here.


class ReviewList(generics.ListCreateAPIView):
    """
    API views for the Review model.

    Attributes:
        ReviewList: A view to list and create reviews.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'playdate_post',
        'user__username'
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API views for the Review model.

    Attributes:
        ReviewDetail: A view to retrieve, update, and delete reviews.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
