from django.urls import path
from blog import views

urlpatterns = [
    path('blog_home/', views.blog_home, name='blog_home'),
    path('blog_post/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog_category/<str:category>/', views.blog_category, name='blog_category')
]