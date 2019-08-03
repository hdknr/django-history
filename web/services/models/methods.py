from django.utils.functional import cached_property
import gkeepapi


class GoogleKeep(object):

    @property
    def current(self):
        self._keep = gkeepapi.Keep()
        if self.token:
            self._keep.resume(self.login_name, self.token)
        else:
            self._keep.login(self.login_name, self.login_password)
            self.token = getMasterToken()
            self.save()
        return self._keep
