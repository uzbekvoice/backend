from rest_framework import serializers


class RecordVoiceSerializer(serializers.Serializer):
    """Serializer for record-voice function"""
    author = serializers.IntegerField()
