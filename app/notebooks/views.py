from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Notebooks
from .serializers import NotebooksSerializer


class NotebooksList(APIView):
    def post(self, request):
        """Creates a new notebook

        Args:
             request (any): Data that cames from the request

        Returns:
           Response: returns serializer data and http status
        """
        serializer = NotebooksSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Retrieves all notebooks

        Args:
            request (any): Data that cames from the request

        Returns:
            Response: returns serializer data and http status
        """
        notebooks = Notebooks.objects.all().order_by('created_at')
        serializer = NotebooksSerializer(notebooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotebooksDetails(APIView):
    def get(self, request, pk):
        """Retrieves a specific notebook by ID

        Args:
            request (any): Data that cames from the request
            pk (int): Public key (ID) of the notebook to get

        Returns:
            Response: returns serializer data and http status
        """
        notebook = Notebooks.objects.filter(pk=pk).first()
        if (notebook):
            serializer = NotebooksSerializer(notebook)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested notebook was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """Updates a specific notebook by ID

        Args:
            request (any): Data that cames from the request
            pk (int): Public key (ID) of the notebook to get

        Returns:
            Response: returns serializer data and http status
        """
        notebook = Notebooks.objects.filter(pk=pk).first()
        serializer = NotebooksSerializer(notebook, request.data)

        if (notebook == None):
            return Response("The requested notebook was not found or does not exists", status=status.HTTP_404_NOT_FOUND)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deletes a specific notebook by ID

        Args:
            request (any): Data that cames from the request
            pk (int): Public key (ID) of the notebook to get

        Returns:
            Response: returns serializer data and http status
        """
        notebook = Notebooks.objects.filter(pk=pk).first()
        if (notebook):
            serializer = NotebooksSerializer(notebook)
            notebook.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested notebook was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)
