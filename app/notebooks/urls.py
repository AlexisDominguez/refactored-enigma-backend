from django.urls import path
from app.notebooks.views import NotebooksDetails, NotebooksList

urlpatterns = [
    path("api/notebooks/", NotebooksList.as_view()),
    path("api/notebooks/<int:pk>/", NotebooksDetails.as_view())
]
