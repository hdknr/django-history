from django.urls import path, include
from . import views


urlpatterns = [
    path('api/', include('histories.api.urls')),
    path('<int:id>', views.note_detail, name="histories_note_detail"),
    path('', views.note_index, name="histories_note_index"),
]