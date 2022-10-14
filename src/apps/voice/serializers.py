from rest_framework import serializers

from .models import Voice, VoiceChecker
from apps.user.models import User
from apps.sentence.models import Sentence


class VoiceSerializer(serializers.Serializer):
    """Serializer class for model Voice"""
    audio_url = serializers.URLField()
    author = serializers.IntegerField()
    sentence = serializers.IntegerField()


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

