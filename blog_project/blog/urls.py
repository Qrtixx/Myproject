from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('category/<slug:slug>/', views.category_articles, name='category'),
]
