"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .serializers import UserViewSet
from accounts.serializer import AccountViewSet
from blog.serializer import PostViewSet,CategoryViewSet,CommentViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'blog/post', PostViewSet)
router.register(r'blog/category', CategoryViewSet)
router.register(r'blog/comment', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('',include('blog.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
