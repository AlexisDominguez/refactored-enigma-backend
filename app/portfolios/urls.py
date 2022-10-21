from django.urls import path
from .views import PortfolioDetails, PortfolioList

urlpatterns = [
    path("api/portfolios/", PortfolioList.as_view()),
    path("api/portfolios/<int:pk>/", PortfolioDetails.as_view())
]
