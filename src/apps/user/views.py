import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from core.view_kit import ViewKit

from core.settings import PROJECT_NAME


logger = logging.getLogger(PROJECT_NAME)


class UserViewSet(ModelViewSet, ViewKit):
    """View Set class which implements CRUD Endpoints for User model"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    model = User

    @classmethod
    def build_result_data(cls, user_obj: User):
        """Method to build JSONed data to put in response body"""
        return {
            "id": user_obj.id,
            "full_name": user_obj.full_name,
            "tg_id": user_obj.tg_id,
            "gender": user_obj.gender,
            "year_of_birth": user_obj.year_of_birth,
            "accent_region": user_obj.accent_region,
            "native_language": user_obj.native_language,
            "created_at": user_obj.created_at,
            "updated_at": user_obj.updated_at
        }

    def get(self, request, pk=None, *args, **kwargs):
        """Method to handle GET Request"""
        status_code = status.HTTP_204_NO_CONTENT
        result_data = None

        if pk:
            try:
                result_data = self.build_result_data(self.get_query_manager().get(pk=pk))
                status_code = status.HTTP_200_OK
            except Exception as ex:
                logger.warning(f"{ex}: Could not get User object by ID: {pk}.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def list(self, request, *args, **kwargs):
        """Method to handle GET Request for List view"""
        status_code = status.HTTP_204_NO_CONTENT
        result_data = None

        try:
            result_data = [self.build_result_data(user_obj) for user_obj in self.get_query_manager().all()]
            status_code = status.HTTP_200_OK
        except Exception as ex:
            logger.warning(f"{ex}: Could not get list of User objects.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def post(self, request):
        """Method to handle POST Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                result_data = self.build_result_data(self.get_query_manager().create(**serializer.data))
                status_code = status.HTTP_201_CREATED
            except Exception as ex:
                logger.warning(f"{ex}: Could not create User object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def put(self, request, pk=None, *args, **kwargs):
        """Method to handle PUT Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = UserSerializer(request.user, data=request.data, partial=False)
            if serializer.is_valid():
                try:
                    result_data = User.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update User object and save it to DB.")
                    logger.warning(f"{ex}: Could not update User object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def patch(self, request, pk=None, *args, **kwargs):
        """Method to handle PATCH Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = UserSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                try:
                    result_data = User.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update User object and save it to DB.")
                    logger.warning(f"{ex}: Could not update User object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def delete(self, request, pk=None):
        """Method to handle DELETE Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None

        if pk:
            try:
                self.get_query_manager().get(pk=pk).delete()
                status_code = status.HTTP_200_OK
            except Exception as ex:
                logger.warning(f"{ex}: Could not delete User object with ID: {pk}.")

        return Response(self.build_response(status_code, result_data), status=status_code)
