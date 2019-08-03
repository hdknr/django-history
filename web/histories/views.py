from django.shortcuts import render
from . import models


def note_index(request):
    context = dict(
        instances=None,
    )
    return render(request, 'histories/note/index.html', context=context)


def note_detail(request, id):
    context = dict(
        instances=models.Note.objects.filter(id=id).first(),
    )
    return render(request, 'histories/note/detail.html', context=context)