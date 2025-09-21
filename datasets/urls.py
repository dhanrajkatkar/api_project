from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatasetViewSet

# Create a router and register our viewset with it.
# The DefaultRouter automatically generates the URL patterns for our ViewSet.
router = DefaultRouter()
router.register(r'datasets', DatasetViewSet, basename='dataset')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
