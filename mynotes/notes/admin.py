from django.contrib import admin

from .models import Note, Book, UserBookRelation


@admin.register(Note)
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'date_pub')
    readonly_fields = ('date_pub',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'author_name', 'owner')
    list_display = ('name', 'price', 'author_name', 'owner', 'id')


@admin.register(UserBookRelation)
class UserBookRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'like', 'in_bookmarks', 'rate')
