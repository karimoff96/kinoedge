from django.urls import path
from . import views
urlpatterns = [
    path('actor/', views.ActorListAPIView.as_view()),
    path('actor/<int:actor_id>', views.ActorDetailAPIView.as_view())
    
]
