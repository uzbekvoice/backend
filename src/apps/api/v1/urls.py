from django.urls import path

from apps.user.views import UserViewSet


urlpatterns = [
    # User Endpoints
    path(
        "user",
        UserViewSet.as_view(
            {
                "get": "list",
                "post": "post",
            },
        )
    ),
    path(
        "user/<int:pk>",
        UserViewSet.as_view(
            {
                "get": "get",
                "delete": "delete"
            },
        )
    ),
]
