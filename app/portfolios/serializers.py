from rest_framework import serializers
from .models import Portfolios


class PortfoliosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolios
        fields = "__all__"
        reat_only_fields = ("id", "created_at", "updated_at")
