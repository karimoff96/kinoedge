from django.urls import path
from . import views

urlpatterns = [
    path('studio/', views.StudioListAPIView.as_view()),
    path('studio/<int:studio_id>/', views.StudioDetailAPIView.as_view()),
]