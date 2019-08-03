Chromeの本日のリンク取り込み:

~~~bash 
$ python manage.py chrome stock
~~~

jupyter nodebookの起動:

~~~bash
$ python manage.py shell_plus --notebook
~~~

jupyter lab:

~~~bash 
PYTHONPATH=$PWD:$PYTHONPATH DJANGO_SETTINGS_MODULE=app.settings jupyter lab --notebook-dir /Users/hide/Documents/Tech/annotated-django/markdown/python/anaconda/notebook
~~~

ブラウザでアクセス:

- http://localhost:8888/tree
- http://localhost:8888/notebooks/sample.ipynb