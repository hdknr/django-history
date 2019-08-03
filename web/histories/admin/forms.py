from django import forms
from histories import models


class NoteForm(forms.ModelForm):
    url = forms.URLField(required=False)

    class Meta:
        model = models.NoteLink
        exclude = ['']