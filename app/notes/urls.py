from django.urls import path
from app.notes.views import NotesDetails, NotesList

urlpatterns = [
    path("api/notes/", NotesList.as_view()),
    path("api/notes/<int:pk>/", NotesDetails.as_view())
]
