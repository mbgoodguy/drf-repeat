from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteModelViewSet

app_name = 'notes'

router = DefaultRouter()
router.register(r'notes', NoteModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
