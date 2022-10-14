import logging

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer
from core.settings import PROJECT_NAME


logger = logging.getLogger(PROJECT_NAME)


@api_view(['GET'])
def user_list(request, pk=None):
    model = User.objects.all()
    serializer = UserSerializer(model, many=True)

    if pk:
        model = get_object_or_404(model, tg_id=pk)
        serializer = UserSerializer(model, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def user_update(request, pk):
    model = User.objects.get(tg_id=pk)
    serializer = UserSerializer(instance=model, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def user_delete(request, pk):
    model = User.objects.get(tg_id=pk)
    model.delete()
    return Response('deleted')

