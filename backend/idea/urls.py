from django.urls import path
from idea import views

urlpatterns = [
    # Get all ideas
    path('ideas/', views.get_ideas),
    # Get a single idea from its id
    path('ideas/<int:pk>/', views.idea_detail),
]