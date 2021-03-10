from django.urls import path
from idea import views

urlpatterns = [
    path('ideas/', views.get_ideas),
    path('ideas/<int:pk>/', views.idea_detail),
]