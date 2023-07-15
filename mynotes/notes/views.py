from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Note, UserBookRelation, Book
from .permissions import IsOwnerOrStaffreadOnly
from .serializers import NoteSerializer, UserBookRelationSerializer, BookSerializer


class NoteModelViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class BooksModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrStaffreadOnly]
    lookup_field = 'slug'  # Указываем slug в качестве идентификатора

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserBookRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = 'book'

    def get_object(self):
        obj, _ = UserBookRelation.objects.get_or_create(user=self.request.user,
                                                        book_id=self.kwargs['book']
                                                        )
        return obj
