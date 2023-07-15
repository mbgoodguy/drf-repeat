from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Note, UserBookRelation, Book


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    owner = serializers.StringRelatedField()  # Здесь указываем, что поле "owner" должно использовать метод __str__ модели User
    owner_id = serializers.IntegerField(source='owner.id', read_only=True)

    class Meta:
        fields = "__all__"
        model = Book


class UserBookRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('user', 'book', 'like', 'in_bookmarks')

    def create(self, validated_data):
        # Проверяем, существует ли уже отношение между пользователем и книгой
        user = validated_data['user']
        book = validated_data['book']

        try:
            # Если отношение уже существует, обновляем его
            relation = UserBookRelation.objects.get(user=user, book=book)
            relation.like = validated_data.get('like', relation.like)
            relation.in_bookmarks = validated_data.get('in_bookmarks', relation.in_bookmarks)
            relation.save()
            return relation
        except UserBookRelation.DoesNotExist:
            # Если отношение не существует, создаем новое
            return UserBookRelation.objects.create(**validated_data)


class BookDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    author_name = serializers.CharField(max_length=100)
    owner = serializers.CharField(source='owner.username')
    owner_id = serializers.IntegerField(source='owner.id')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.save()
        return instance
