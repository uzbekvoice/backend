from rest_framework import serializers

from apps.user.models import User
from apps.sentence.models import Sentence


class SentenceSerializer(serializers.Serializer):
    text = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all()
    )
    reads_count = serializers.IntegerField()
    is_valid = serializers.BooleanField()
    invalidity_reason = serializers.IntegerField()



