from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Create your views here.


class CommentList(generics.ListCreateAPIView):
    """
    Views for handling comment-related operations.
    Attributes:
        CommentList: View for listing and creating comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'playdate_post',
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Views for handling comment-related operations.
    Attributes:
        CommentDetail: View for retrieving, updating, and deleting a specific comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
