from logging import NOTSET
from django.urls import path
from app.notes.views import NotesList

urlpatterns = [
    path("api/notes/", NotesList.as_view())
]
