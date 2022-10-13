from rest_framework import serializers
from .models import Notebooks


class NotebooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebooks
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
