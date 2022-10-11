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

]
