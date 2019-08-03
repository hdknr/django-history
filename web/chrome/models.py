# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from . import methods, querysets


class Downloads(models.Model):
    guid = models.TextField()  # This field type is a guess.
    current_path = models.TextField()  # This field type is a guess.
    target_path = models.TextField()  # This field type is a guess.
    start_time = models.IntegerField()
    received_bytes = models.IntegerField()
    total_bytes = models.IntegerField()
    state = models.IntegerField()
    danger_type = models.IntegerField()
    interrupt_reason = models.IntegerField()
    hash = models.BinaryField()
    end_time = models.IntegerField()
    opened = models.IntegerField()
    last_access_time = models.IntegerField()
    transient = models.IntegerField()
    referrer = models.TextField()  # This field type is a guess.
    site_url = models.TextField()  # This field type is a guess.
    tab_url = models.TextField()  # This field type is a guess.
    tab_referrer_url = models.TextField()  # This field type is a guess.
    http_method = models.TextField()  # This field type is a guess.
    by_ext_id = models.TextField()  # This field type is a guess.
    by_ext_name = models.TextField()  # This field type is a guess.
    etag = models.TextField()  # This field type is a guess.
    last_modified = models.TextField()  # This field type is a guess.
    mime_type = models.CharField(max_length=255)
    original_mime_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'downloads'


class DownloadsSlices(models.Model):
    download_id = models.IntegerField()
    offset = models.IntegerField()
    received_bytes = models.IntegerField()
    finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'downloads_slices'
        unique_together = (('download_id', 'offset'),)


class DownloadsUrlChains(models.Model):
    chain_index = models.IntegerField()
    url = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'downloads_url_chains'
        unique_together = (('id', 'chain_index'),)


class KeywordSearchTerms(models.Model):
    keyword_id = models.IntegerField()
    url_id = models.IntegerField()
    lower_term = models.TextField()  # This field type is a guess.
    term = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'keyword_search_terms'


class Meta(models.Model):
    key = models.TextField(unique=True)  # This field type is a guess.
    value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'meta'


class SegmentUsage(models.Model):
    segment_id = models.IntegerField()
    time_slot = models.IntegerField()
    visit_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'segment_usage'


class Segments(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    url_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'segments'


class TypedUrlSyncMetadata(models.Model):
    storage_key = models.IntegerField()
    value = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typed_url_sync_metadata'


class Urls(models.Model, methods.Urls):
    url = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    visit_count = models.IntegerField()
    typed_count = models.IntegerField()
    last_visit_time = models.IntegerField()
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'urls'

    objects = querysets.UrlsQuerySet.as_manager()

    def __str__(self):
        return self.title or self.url


class VisitSource(models.Model):
    source = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'visit_source'


class Visits(models.Model):
    url = models.ForeignKey(Urls, db_column="url", on_delete=models.CASCADE)
    visit_time = models.IntegerField()
    from_visit = models.IntegerField(blank=True, null=True)
    transition = models.IntegerField()
    segment_id = models.IntegerField(blank=True, null=True)
    visit_duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'visits'
