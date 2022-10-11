import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Sentence
from apps.user.models import User
from .serializers import SentenceSerializer
from core.settings import PROJECT_NAME


logger = logging.getLogger(PROJECT_NAME)


@api_view(['GET'])
def sentence_list(request, pk=None):
    model = Sentence.objects.all()
    serializer = SentenceSerializer(model, many=True)

    if pk:
        model = model.get(pk=pk)
        serializer = SentenceSerializer(model, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def sentence_create(request):
    serializer = SentenceSerializer(data=request.data, partial=True)
    print(serializer.is_valid())
    if serializer.is_valid():
        text = serializer.data['text']
        id = serializer.data['author']
        invalidity_reason = serializer.data['invalidity_reason']
        is_valid = serializer.data['is_valid']

        author = User.objects.get(id=id)
        Sentence.objects.create(
            text=text,
            author=author,
            invalidity_reason=invalidity_reason,
            is_valid=is_valid
        )
    return Response(serializer.data)


@api_view(["POST"])
def sentence_update(request, pk):
    model = Sentence.objects.get(pk=pk)
    serializer = SentenceSerializer(instance=model, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def sentence_delete(request, pk):
    model = Sentence.objects.get(pk=pk)
    model.delete()
    return Response('deleted')



