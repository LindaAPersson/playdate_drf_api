from django.urls import path
from contact import views
"""
    URL patterns for the contact app.
"""
urlpatterns = [
    path('contact/', views.ContactList.as_view()),
    path('contact/<int:pk>/', views.ContactDetail.as_view()),
]
