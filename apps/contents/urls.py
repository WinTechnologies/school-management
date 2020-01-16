from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v


router = DefaultRouter(trailing_slash=False)
router.register(r'news', v.NewsViewSet)
router.register(r'notifications', v.NotificationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
