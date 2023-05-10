from django.urls import path
from . import views

urlpatterns = [
    
    path('category/', views.CategoryListAPIView.as_view()),
    path('category/<int:category_id>/', views.CategoryDetailAPIView.as_view()),
    path('genre/', views.GenreListAPIView.as_view()),
    path('genre/<int:genre_id>/', views.GenreDetailAPIView.as_view()),
    path('movie/', views.MovieListAPIVIew.as_view())
]