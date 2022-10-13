from django.urls import path
from app.notebooks.views import ping

urlpatterns = [
    path("api/notebooks/", ping)
]
