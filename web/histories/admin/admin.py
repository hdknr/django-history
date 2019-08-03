from django.contrib import admin
from histories import models, signals
from . import inlines, forms


@admin.register(models.Ignore)
class IgnoreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Ignore._meta.fields]
    list_filter = ['is_domain']
    search_fields = ['pattern']


@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Domain._meta.fields]
    list_filter = ['stock']
    search_fields = ['hostname']


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Link._meta.fields] 
    list_filter = ['domain']
    search_fields = ['domain__hostname', 'title', 'url']
    raw_id_fields = ['domain']
    readonly_fields = ['markdown']
    inlines = [
        inlines.LinkTagItemInline,
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        signals.update_link.send(sender=self, instance=obj)


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Note._meta.fields]
    inlines = [inlines.NoteLinkInline]
    form = forms.NoteForm
    search_fields = ['title', 'text', 'notelink__link__title']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        notelink = obj.add_link(form.cleaned_data.get('url', None))
        if notelink:
            signals.update_link.send(sender=self, instance=notelink.link)
 