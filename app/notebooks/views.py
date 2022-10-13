from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Notebooks
from .serializers import NotebooksSerializer


class NotebooksList(APIView):
    def post(self, request):
        serializer = NotebooksSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notebooks = Notebooks.objects.all().order_by('created_at')
        serializer = NotebooksSerializer(notebooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotebooksDetails(APIView):
    def get(self, request, pk):
        notebook = Notebooks.objects.filter(pk=pk).first()
        if (notebook):
            serializer = NotebooksSerializer(notebook)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested notebook was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        notebook = Notebooks.objects.filter(pk=pk).first()
        serializer = NotebooksSerializer(notebook, request.data)

        if (notebook == None):
            return Response("The requested notebook was not found or does not exists", status=status.HTTP_404_NOT_FOUND)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notebook = Notebooks.objects.filter(pk=pk).first()
        if (notebook):
            serializer = NotebooksSerializer(notebook)
            notebook.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested notebook was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)
