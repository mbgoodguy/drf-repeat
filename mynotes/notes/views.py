from rest_framework.viewsets import ModelViewSet

from .models import Note
from .serializers import NoteSerializer


class NoteModelViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
