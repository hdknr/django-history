# pip install markdown for DRF testing
# python manage.py test --settings=app.test_settings
from .settings import *
# https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-tests-using-tox

INSTALLED_APPS += [
    'django_nose',
]
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',  # coverage を取る
    '--cover-html',
    '--cover-package=chrome,histories',
    '--nocapture',
    '--nologcapture',
]