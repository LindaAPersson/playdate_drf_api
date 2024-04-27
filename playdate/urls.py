from django.urls import path
from playdate import views
"""
    URL patterns for playdate-related views.
"""
urlpatterns = [
    path('playdate/', views.PlaydateList.as_view()),
    path('playdate/<int:pk>/', views.PlaydateListDetail.as_view()),
]
