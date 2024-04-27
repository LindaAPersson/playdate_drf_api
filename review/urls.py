from django.urls import path
from review import views
"""
    URL patterns for review-related views.
"""
urlpatterns = [
    path('review/', views.ReviewList.as_view()),
    path('review/<int:pk>/', views.ReviewDetail.as_view()),
]
