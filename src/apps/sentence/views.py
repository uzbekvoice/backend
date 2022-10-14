import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Sentence
from apps.user.models import User
from .serializers import SentenceSerializer
from core.settings import PROJECT_NAME


logger = logging.getLogger(PROJECT_NAME)


def build_respone_data(sentence_obj: Sentence):
    return {
        'id': sentence_obj.id,
        'tg_id': sentence_obj.author.tg_id,
        'text': sentence_obj.text,
        'status': sentence_obj.status,
        'is_read': sentence_obj.is_read,
        'created_at': sentence_obj.created_at,
        'updated_at': sentence_obj.updated_at
    }

@api_view(['GET'])
def sentence_list(request, pk=None):
    if pk:
        model = Sentence.objects.get(pk=pk)
        data = build_respone_data(model)
    else:
        model = Sentence.objects.all()
        data = [build_respone_data(sentence_obj) for sentence_obj in model]
    return Response(data=data)


@api_view(['POST'])
def sentence_create(request):
    serializer = SentenceSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        text = serializer.data['text']
        tg_id = serializer.data['tg_id']
        author = User.objects.get(tg_id=tg_id)
        sentence = Sentence.objects.create(text=text, author=author)
        return Response(build_respone_data(sentence))
    return Response(status=400)


@api_view(["POST"])
def sentence_update(request, pk):
    model = Sentence.objects.filter(pk=pk)
    serializer = SentenceSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        text = serializer.data['text']
        tg_id = serializer.data['tg_id']
        author = User.objects.get(tg_id=tg_id)
        model.update(text=text, author=author)

    return Response(status=200)


@api_view(["DELETE"])
def sentence_delete(request, pk):
    model = Sentence.objects.get(pk=pk)
    model.delete()
    return Response('deleted')



