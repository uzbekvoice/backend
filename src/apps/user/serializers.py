from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """Serializer class for model User"""
    full_name = serializers.CharField(max_length=200)
    tg_id = serializers.IntegerField()
    gender = serializers.CharField(max_length=1)
    year_of_birth = serializers.CharField(max_length=4)
    accent_region = serializers.CharField(max_length=18)
    native_language = serializers.CharField(max_length=2)
