from django.urls import reverse


class Note(object):

    def add_link(self, url):
        if url:
            from .models import Domain
            domain = Domain.objects.get_for_link(url)
            link, created = domain.link_set.get_or_create(url=url)
            notelink, created = self.notelink_set.get_or_create(link=link)
            return notelink

    def get_absolute_url(self):
        return reverse('histories_note_detail', kwargs={'id': self.id}) 


class Link(object):

    @property
    def markdown(self):
        title = self.title.replace('|', '-')   # STOP Jekyll making tables
        return f"[{title}]({self.url})"