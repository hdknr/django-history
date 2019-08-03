from django.contrib import admin
from django.utils.html import mark_safe as _S
from chrome import models
from . import forms


@admin.register(models.Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ['id', 'hostname', 'title', 'last_visit_at', ]
    search_fields = ['url', 'title']
    readonly_fields = ['anchor', 'markdown']
    form = forms.UrlsForm
    actions = ['remove_ignores', 'stock']

    def anchor(self, obj):
        return _S(f'<a href="{obj.url}">{obj.title}</a>')

    anchor.short_description = "URL"

    def save_model(self, request, obj, form, change):
        is_stocked = form.cleaned_data.get('is_stocked', False)
        super().save_model(request, obj, form, change)
        obj.stock(enabled=is_stocked)

    def remove_ignores(self, request, queryset):
        models.Urls.objects.remove_ignores()

    remove_ignores.short_description = "Remove unnecessary urls"

    def stock(self, request, queryset):
        for url in queryset:
            url.stock()
            url.delete()

    stock.short_description = "Stock urls"


