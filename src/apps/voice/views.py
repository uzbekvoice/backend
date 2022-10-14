import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Voice, VoiceChecker
from apps.user.models import User
from core.settings import PROJECT_NAME
from .serializers import VoiceSerializer, VoiceCheckerSerializer
from apps.sentence.models import Sentence


logger = logging.getLogger(PROJECT_NAME)


def build_respone_data(voice_obj: Voice):
    return {
        'id': voice_obj.id,
        'audio_url': voice_obj.audio_url,
        'tg_id': voice_obj.author.tg_id,
        'text': voice_obj.sentence.text,
        'status': voice_obj.status,
        'created_at': voice_obj.created_at,
        'updated_at': voice_obj.updated_at
    }


# Voice CRUD
@api_view(['GET'])
def voice_list(request, pk=None):
    if pk:
        model = Voice.objects.get(pk=pk)
        data = build_respone_data(model)
    else:
        model = Voice.objects.all()
        data = [build_respone_data(voice_obj) for voice_obj in model]
    return Response(data=data)


@api_view(['POST'])
def voice_create(request):
    serializer = VoiceSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        audio_url = serializer.data['audio_url']
        author_tg_id = serializer.data['author']
        sentence_id = serializer.data['sentence']
        author = User.objects.get(tg_id=author_tg_id)
        sentence = Sentence.objects.get(id=sentence_id)
        Voice.objects.create(
            audio_url=audio_url,
            author=author,
            sentence=sentence
        )
        Sentence.objects.filter(id=sentence_id).update(is_read=True)
    return Response(serializer.data)


@api_view(["POST"])
def voice_update(request, pk):
    model = Voice.objects.filter(pk=pk)
    serializer = VoiceSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        audio_url = serializer.data['audio_url']
        author_tg_id = serializer.data['author']
        sentence_id = serializer.data['sentence']
        author = User.objects.get(tg_id=author_tg_id)
        sentence = Sentence.objects.get(id=sentence_id)
        model.update(audio_url=audio_url, author=author, sentence=sentence)
    return Response(serializer.data)


@api_view(["DELETE"])
def voice_delete(request, pk):
    model = Voice.objects.get(pk=pk)
    model.delete()
    return Response('deleted')


# VoiceChecker CRUD
@api_view(['GET'])
def voice_checker_list(request, pk=None):
    model = VoiceChecker.objects.all()
    serializer = VoiceCheckerSerializer(model, many=True)

    if pk:
        model = model.get(pk=pk)
        serializer = VoiceCheckerSerializer(model, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def voice_checker_create(request):
    serializer = VoiceCheckerSerializer(data=request.data)
    if serializer.is_valid():
        author_id = serializer.data['author']
        voice_id = serializer.data['voice_id']

        author = User.objects.get(id=author_id)
        voice = Voice.objects.get(id=voice_id)
        voice_checker = VoiceChecker.objects.create(
            author=author,
            voice=voice.id
        )
        print(voice_checker)
    return Response(serializer.data)


@api_view(["POST"])
def voice_checker_update(request, pk):
    model = VoiceChecker.objects.get(pk=pk)
    serializer = VoiceCheckerSerializer(instance=model, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def voice_checker_delete(request, pk):
    model = VoiceChecker.objects.get(pk=pk)
    model.delete()
    return Response('deleted')
