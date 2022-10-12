from rest_framework import serializers

from .models import Voice, VoiceChecker
from apps.user.models import User
from apps.sentence.models import Sentence


class VoiceSerializer(serializers.ModelSerializer):
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
    is_valid = serializers.BooleanField()
    invalidity_reason = serializers.IntegerField()

    class Meta:
        model = Voice
        fields = "__all__"


class VoiceCheckerSerializer(serializers.ModelSerializer):
    """Serializer class for model VoiceChecker"""
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all()
    )
    voice_id = serializers.IntegerField()

    class Meta:
        model = VoiceChecker
        fields = "__all__"

