from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for model User"""
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']



