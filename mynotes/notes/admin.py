from django.contrib import admin

from .models import Note


@admin.register(Note)
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'date_pub')
    readonly_fields = ('date_pub',)
