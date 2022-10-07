import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from core.view_kit import ViewKit
from .models import Voice, VoiceChecker
from .serializers import VoiceSerializer, VoiceCheckerSerializer

from core.settings import PROJECT_NAME

logger = logging.getLogger(PROJECT_NAME)


class VoiceViewSet(ModelViewSet, ViewKit):
    """View Set class which implements CRUD Endpoints for Voice model"""
    permission_classes = [AllowAny]
    serializer_class = VoiceSerializer
    model = Voice

    @classmethod
    def build_result_data(cls, voice_obj: Voice):
        """Method to build JSONed data to put in response body"""
        return {
            "id": voice_obj.id,
            "audio_url": voice_obj.audio_url,
            "author": voice_obj.author,
            "sentence": voice_obj.sentence,
            "checks_count": voice_obj.checks_count,
            "is_valid": voice_obj.is_valid,
            "invalidity_reason": voice_obj.invalidity_reason,
            "created_at": voice_obj.created_at,
            "updated_at": voice_obj.updated_at
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
                logger.warning(f"{ex}: Could not get Voice object by ID: {pk}.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def list(self, request, *args, **kwargs):
        """Method to handle GET Request for List View"""
        status_code = status.HTTP_204_NO_CONTENT
        result_data = None

        try:
            result_data = [self.build_result_data(voice_obj) for voice_obj in self.get_query_manager().all()]
            status_code = status.HTTP_200_OK
        except Exception as ex:
            logger.warning(f"{ex}: Could not get list of Voice objects.")

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
                logger.warning(f"{ex}: Could not create Voice object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def put(self, request, pk=None, *args, **kwargs):
        """Method to handle PUT Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = VoiceSerializer(request.user, data=request.data, partial=False)
            if serializer.is_valid():
                try:
                    result_data = Voice.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update Voice object and save it to DB.")
                    logger.warning(f"{ex}: Could not update Voice object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def patch(self, request, pk=None, *args, **kwargs):
        """Method to handle PATCH Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = VoiceSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                try:
                    result_data = Voice.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update Voice object and save it to DB.")
                    logger.warning(f"{ex}: Could not update Voice object and save it to DB.")

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
                logger.warning(f"{ex}: Could not delete Voice object with ID: {pk}")

        return Response(self.build_response(status_code, result_data), status=status_code)


class VoiceCheckerViewSet(ModelViewSet, ViewKit):
    """View Set class which implements CRUD Endpoints for VoiceChecker model"""
    permission_classes = [AllowAny]
    serializer_class = VoiceCheckerSerializer
    model = VoiceChecker

    @classmethod
    def build_result_data(cls, voice_checker_obj: VoiceChecker):
        """Method to build JSONed data to put in response body"""
        return {
            "id": voice_checker_obj.id,
            "voice": voice_checker_obj.voice,
            "author": voice_checker_obj.author,
            "created_at": voice_checker_obj.created_at,
            "updated_at": voice_checker_obj.updated_ad
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
                logger.warning(f"{ex}: Could not get VoiceChecker object by ID: {pk}.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def list(self, request, *args, **kwargs):
        """Method to handle GET Request for List View"""
        status_code = status.HTTP_204_NO_CONTENT
        result_data = None

        try:
            result_data = [self.build_result_data(voice_checker_obj) for voice_checker_obj in self.get_query_manager().all()]
            status_code = status.HTTP_200_OK
        except Exception as ex:
            logger.warning(f"{ex}: Could not get list of VoiceChecker objects.")

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
                logger.warning(f"{ex}: Could not create VoiceChecker object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def put(self, request, pk=None, *args, **kwargs):
        """Method to handle PUT Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = VoiceCheckerSerializer(request.user, data=request.data, partial=False)
            if serializer.is_valid():
                try:
                    result_data = VoiceChecker.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update VoiceChecker object and save it to DB.")
                    logger.warning(f"{ex}: Could not update VoiceChecker object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def patch(self, request, pk=None, *args, **kwargs):
        """Method to handle PATCH Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = VoiceCheckerSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                try:
                    result_data = VoiceChecker.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update VoiceChecker object and save it to DB.")
                    logger.warning(f"{ex}: Could not update VoiceChecker object and save it to DB.")

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
                logger.warning(f"{ex}: Could not delete VoiceChecker object with ID: {pk}")

        return Response(self.build_response(status_code, result_data), status=status_code)

