from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.page_detail, name="pages_page_detail"),
]