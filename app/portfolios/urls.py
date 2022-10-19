from django.urls import path
from .views import ping

urlpatterns = [
    path("api/portfolios/", ping, name="ping")
]
