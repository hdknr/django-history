from django.contrib import admin
from histories import models
from mytaggit.admin.inlines import GenericTaggedItemInline
from . import forms


class NoteLinkInline(admin.TabularInline):
    model = models.NoteLink
    fields = []
    extra = 0
    raw_id_fields = ['link']


class LinkTagItemInline(GenericTaggedItemInline):
    exclude = ['tag', 'value', 'users']
