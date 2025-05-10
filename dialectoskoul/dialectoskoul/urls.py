"""
URL configuration for dialectoskoul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from skoulApi.views import *
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViews, basename='users')
router.register(r'rules', RulesViewSet, basename='rules')
router.register(r'user-rules', UserJoinRules, basename='user')
router.register(r'pack', PackViewset, basename='pack')
router.register(r'classes', ClassesViewset, basename='classes')
router.register(r'level', LevelClassViewSet, basename='levels')
router.register(r'affectation', affectationStudentViewset, basename='affectation')
router.register(r'diffusion-list', diffusionListViewset, basename='diffusion-list')
router.register(r'APILogEntry', APILogEntryViewset, basename='APILogEntry')
router.register(r'send-email', EmailViewset, basename="send-email")

urlpatterns = [
    path('api/', include(router.urls)),  # Inclure les URLs générées par Django REST Framework
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/dj_rest_auth/', include('dj_rest_auth.urls')),
    # path('api/token/', obtain_auth_token, name='api_token_auth'),
]
