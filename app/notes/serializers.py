from dataclasses import fields
from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
