from rest_framework import serializers

from apps.sentence.models import Sentence


class SentenceSerializer(serializers.Serializer):
    """Serializer class for model Sentence"""
    text = serializers.CharField()
    tg_id = serializers.IntegerField()