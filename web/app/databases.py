''' DatabaseRouter
'''


class DatabaseRouter(object):
    _maps = {
        'chrome': {
            'apps': ['chrome'],
        },
    }

    def get_database(self, model, **hints):
        for db, conf in self._maps.items():
            if model._meta.app_label in conf['apps']:
                return db
        return 'default'

    def db_for_read(self, model, **hints):
        return self.get_database(model, **hints)

    def db_for_write(self, model, **hints):
        return self.get_database(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        for db, conf in self._maps.items():
            if app_label in conf['apps']:
                return db
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db1, db2 = [self.get_database(o) for o in [obj1, obj2]]

        if db1 == db2 and db1:
            return db1

        return None

    @classmethod
    def router(cls):
        return "{0}.{1}".format(cls.__module__, cls.__name__)
