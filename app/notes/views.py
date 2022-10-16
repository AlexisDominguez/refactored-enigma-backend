from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Notes
from .serializers import NotesSerializer


class NotesList(APIView):
    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notes = Notes.objects.all().order_by('created_at')
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotesDetails(APIView):
    def get(self, request, pk):
        note = Notes.objects.filter(pk=pk).first()
        if (note):
            serializer = NotesSerializer(note)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested note was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        note = Notes.objects.filter(pk=pk).first()
        serializer = NotesSerializer(note, request.data)

        if (note == None):
            return Response("The requested note was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = Notes.objects.filter(pk=pk).first()
        if (note):
            serializer = NotesSerializer(note)
            note.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("The requested note was not found or does not exists.", status=status.HTTP_404_NOT_FOUND)


class NotesByNotebook(APIView):
    def get(self, request, notebook_id):
        notes = Notes.objects.filter(
            notebook=notebook_id).order_by('created_at')
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
