from django.urls import path
from app.notes.views import NotesDetails, NotesList, NotesByNotebook

urlpatterns = [
    path("api/notes/", NotesList.as_view()),
    path("api/notes/<int:pk>/", NotesDetails.as_view()),
    path("api/notes-by-notebook/<int:notebook_id>/", NotesByNotebook.as_view())
]
