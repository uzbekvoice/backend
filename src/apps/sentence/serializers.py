from rest_framework import serializers

from .models import Sentence
from apps.user.models import User


class SentenceSerializer(serializers.ModelSerializer):
    """Serializer class for model Sentence"""
    text = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all()
    )
    is_valid = serializers.BooleanField()
    invalidity_reason = serializers.IntegerField()

    class Meta:
        model = Sentence
        fields = "__all__"
