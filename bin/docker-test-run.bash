#!/bin/bash
python /code/web/manage.py test --settings=app.test_settings
cp -r /code/cover /result