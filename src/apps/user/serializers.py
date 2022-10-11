from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for model User"""
    class Meta:
        model = User
        # exclude = ['created_at', 'updated_at']
        fields = '__all__'



