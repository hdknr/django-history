from django import forms
from chrome import models


class UrlsForm(forms.ModelForm):
    is_stocked = forms.BooleanField(required=False)

    class Meta:
        model = models.Urls
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_stocked'].initial = kwargs['instance'].is_stocked