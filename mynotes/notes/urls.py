from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteModelViewSet, BooksModelViewSet

app_name = 'notes'

router = DefaultRouter()
router.register(r'notes', NoteModelViewSet)
router.register(r'books', BooksModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
