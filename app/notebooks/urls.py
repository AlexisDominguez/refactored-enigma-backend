from django.urls import path
from app.notebooks.views import NotebooksDetails, NotebooksList, NotebooksByPortfolio

urlpatterns = [
    path("api/notebooks/", NotebooksList.as_view()),
    path("api/notebooks/<int:pk>/", NotebooksDetails.as_view()),
    path("api/notebooks-by-portfolio/<int:portfolio_id>/",
         NotebooksByPortfolio.as_view())
]
