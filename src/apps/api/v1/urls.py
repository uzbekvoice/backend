from django.urls import path

from apps.user.views import user_list, user_create, user_delete, user_update
from apps.sentence.views import SentenceViewSet
from apps.voice.views import VoiceViewSet, VoiceCheckerViewSet


urlpatterns = [
    # User Endpoints]
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_list, name='user-detail'),
    path('user/create/', user_create, name='user-create'),
    path('user/<int:pk>/update/', user_update, name='user-update'),
    path('user/<int:pk>/delete/', user_delete, name='user-delete'),
]
