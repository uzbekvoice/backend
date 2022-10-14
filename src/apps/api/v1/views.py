from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.user.models import User
from .serializer import RecordVoiceSerializer
from apps.voice.models import Voice, VoiceChecker
from apps.sentence.models import Sentence, SentenceChecker


@api_view(['POST'])
def record_voice(request):
    serializer = RecordVoiceSerializer(data=request.data)
    if serializer.is_valid():
        tg_id = serializer.data['author']
        if User.objects.filter(tg_id__exact=tg_id).exists():
            author = User.objects.get(tg_id__exact=tg_id)
            sentence = Sentence.objects.filter(is_read=False).first()
            data = {
                'tg_id': author.tg_id,
                'sentence_text': sentence.text,
                'sentence_id': sentence.id
            }
            return Response(data=data)
    return HttpResponse(status=400, content='Invalid request')


@api_view(['POST'])
def check_voice(request):
    pass
