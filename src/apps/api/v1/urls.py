from django.urls import path

from apps.user.views import UserViewSet
from apps.sentence.views import SentenceViewSet
from apps.voice.views import VoiceViewSet, VoiceCheckerViewSet


urlpatterns = [
    # User Endpoints
    path(
        "user/",
        UserViewSet.as_view(
            {
                "get": "list",
                "post": "post",
            },
        )
    ),
    path(
        "user/<int:pk>/",
        UserViewSet.as_view(
            {
                "get": "get",
                "delete": "delete"
            },
        )
    ),

    # Voice Endpoints
    path(
        "voice/",
        VoiceViewSet.as_view(
            {
                "get": "list",
                "post": "post",
            },
        )
    ),
    path(
        "voice/<int:pk>/",
        VoiceViewSet.as_view(
            {
                "get": "get",
                "delete": "delete"
            },
        )
    ),

    # VoiceChecker Endpoints
    path(
        "voice-checker/",
        VoiceCheckerViewSet.as_view(
            {
                "get": "list",
                "post": "post",
            },
        )
    ),
    path(
        "voice-checker/<int:pk>/",
        VoiceCheckerViewSet.as_view(
            {
                "get": "get",
                "delete": "delete"
            },
        )
    ),

    # Sentence Endpoints
    path(
        "sentence/",
        SentenceViewSet.as_view(
            {
                "get": "list",
                "post": "post",
            },
        )
    ),
]
