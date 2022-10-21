from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Portfolios
from .serializers import PortfoliosSerializer


class PortfolioList(APIView):
    def post(self, request):
        """Post method to create portfolios

        Args:
            request (any): Data that cames from the request

        Returns:
            Response: returns serializer data and http status
        """
        serializer = PortfoliosSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Gets all portfolios

        Args:
            request (any): Data that cames from the request

        Returns:
             Response: returns serializer data and http status
        """
        portfolios = Portfolios.objects.all().order_by("created_at")
        serializer = PortfoliosSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PortfolioDetails(APIView):
    def get(self, request, pk):
        """Gets a specific portfolio by ID

        Args:
            request (any): Data that cames from the request
            pk (int): Public key (ID) of the portfolio to get

        Returns:
            Response: returns serializer data and http status
        """
        portfolio = Portfolios.objects.filter(pk=pk).first()
        if (portfolio):
            serializer = PortfoliosSerializer(portfolio)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested portfolio was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """Updates a specific portfolio by ID

        Args:
            request (any): Data that cames from the request
            pk (int): Public key (ID) of the portfolio to update

        Returns:
            Response: returns serializer data and http status
        """
        portfolio = Portfolios.objects.filter(pk=pk).first()
        serializer = PortfoliosSerializer(portfolio, request.data)

        if (portfolio == None):
            return Response("The requested portfolio was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """Deletes a specific portfolio by ID

        Args:
            request (any): Data that cames from the request
            pk (int): Public key (ID) of the portfolio to delete

        Returns:
            Response: returns serializer data and http status
        """
        portfolio = Portfolios.objects.filter(pk=pk).first()
        if (portfolio):
            serializer = PortfoliosSerializer(portfolio)
            portfolio.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested portfolio was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)
