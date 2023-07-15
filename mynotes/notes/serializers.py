from rest_framework.serializers import ModelSerializer

from .models import Note, UserBookRelation, Book


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('user', 'book', 'like', 'in_bookmarks', 'rate')
