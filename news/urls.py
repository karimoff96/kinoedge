from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListAPIView.as_view()),
    path('news/<int:news_id>/', views.NewsDetailAPIView.as_view()),
]
