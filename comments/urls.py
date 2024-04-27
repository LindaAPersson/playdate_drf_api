from django.urls import path
from comments import views
"""
URL patterns for comment-related endpoints.
"""
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]
