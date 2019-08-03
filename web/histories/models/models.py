from django.db import models
# from taggit.managers import TaggableManager
from mytaggit.models import TaggableManager
from . import querysets, methods


class Ignore(models.Model):
    pattern = models.CharField(max_length=100)
    is_domain = models.BooleanField(default=False)

    def __str__(self):
        return self.pattern


class Domain(models.Model):
    hostname = models.CharField(max_length=200, unique=True)
    stock = models.BooleanField(default=False)
    description = models.TextField(
        default=None, blank=True, null=True)

    objects = querysets.DomainQuerySet.as_manager()

    def __str__(self):
        return self.hostname


class Link(models.Model, methods.Link):
    domain = models.ForeignKey(
        Domain, 
        null=True, blank=True, default=None, 
        on_delete=models.SET_NULL)
    url = models.URLField()
    title = models.TextField(
        null=True, default=None, blank=True)
    visited_at = models.DateTimeField(
        null=True, default=None, blank=True)
    enabled = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title or self.url


class Note(models.Model, methods.Note):
    title = models.TextField(
        null=True, default=None, blank=True)
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return (self.text and self.text[:20] or '') + '...'


class NoteLink(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE) 
    link = models.ForeignKey(Link, on_delete=models.CASCADE) 
    text = models.TextField(
        null=True, blank=True, default=None)

    class Meta:
        ordering = ['-id']