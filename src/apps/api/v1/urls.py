from django.urls import path

from apps.user.views import (
    user_list,
    user_create,
    user_update,
    user_delete,
)
from apps.sentence.views import (
    sentence_list,
    sentence_create,
    sentence_update,
    sentence_delete,
)

from apps.voice.views import (
    voice_list,
    voice_create,
    voice_update,
    voice_delete,
)

from apps.voice.views import (
    voice_checker_list,
    voice_checker_create,
    voice_checker_update,
    voice_checker_delete,
)

urlpatterns = [
    # User Endpoints
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_list, name='user-detail'),
    path('user/create/', user_create, name='user-create'),
    path('user/<int:pk>/update/', user_update, name='user-update'),
    path('user/<int:pk>/delete/', user_delete, name='user-delete'),

    # Sentence Endpoints
    path('sentence/', sentence_list, name='sentence-list'),
    path('sentence/<int:pk>/', sentence_list, name='sentence-detail'),
    path('sentence/create/', sentence_create, name='sentence-create'),
    path('sentence/<int:pk>/update/', sentence_update, name='sentence-update'),
    path('sentence/<int:pk>/delete/', sentence_delete, name='sentence-delete'),

    # Voice Endpoints
    path('voice/', voice_list, name='voice-list'),
    path('voice/<int:pk>/', voice_list, name='voice-detail'),
    path('voice/create/', voice_create, name='voice-create'),
    path('voice/<int:pk>/update/', voice_update, name='voice-update'),
    path('voice/<int:pk>/delete/', voice_delete, name='voice-delete'),

    # VoiceChecker Endpoints
    path('voice-checker/', voice_checker_list, name='voice-checker-list'),
    path('voice-checker/<int:pk>/', voice_checker_list, name='voice-checker-detail'),
    path('voice-checker/create/', voice_checker_create, name='voice-create'),
    path('voice-checker/<int:pk>/update/', voice_checker_update, name='voice-checker-update'),
    path('voice-checker/<int:pk>/delete/', voice_checker_delete, name='voice-checker-delete'),

]
