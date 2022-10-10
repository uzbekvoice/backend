from rest_framework import serializers

from .models import Voice
from apps.user.models import User
from apps.sentence.models import Sentence


class VoiceSerializer(serializers.Serializer):
    """Serializer class for model Voice"""
    audio_url = serializers.URLField()
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all()
    )
    sentence = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=Sentence.objects.all()
    )
    checks_count = serializers.IntegerField()
    is_valid = serializers.BooleanField()
    invalidity_reason = serializers.IntegerField()


class VoiceCheckerSerializer(serializers.Serializer):
    """Serializer class for model VoiceChecker"""
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all()
    )
    voice = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=Voice.objects.all()
    )


