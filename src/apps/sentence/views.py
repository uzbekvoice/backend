import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.view_kit import ViewKit
from core.settings import PROJECT_NAME
from .models import Sentence
from .serializers import SentenceSerializer


logger = logging.getLogger(PROJECT_NAME)


class SentenceViewSet(ModelViewSet, ViewKit):
    """View Set class which implements CRUD Endpoints for Sentence model"""
    permission_classes = [AllowAny]
    serializer_class = SentenceSerializer
    model = Sentence

    @classmethod
    def build_result_data(cls, sentence_obj: Sentence):
        """Method to build JSONed data to put in response body"""
        return {
            "id": sentence_obj.id,
            "text": sentence_obj.text,
            "author": sentence_obj.author,
            "reads_count": sentence_obj.reads_count,
            "is_valid": sentence_obj.is_valid,
            "invalidity_reason": sentence_obj.invalidity_reason,
            "created_at": sentence_obj.created_at,
            "updated_at": sentence_obj.updated_at
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
                logger.warning(f"{ex}: Could not get Sentence object by ID: {pk}.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def list(self, request, *args, **kwargs):
        """Method to handle GET Request for List View"""
        status_code = status.HTTP_204_NO_CONTENT
        result_data = None

        try:
            result_data = [self.build_result_data(sentence_obj) for sentence_obj in self.get_query_manager().all()]
            status_code = status.HTTP_200_OK
        except Exception as ex:
            logger.warning(f"{ex}: Could not get list of Sentence objects.")

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
                logger.warning(f"{ex}: Could not create Sentence object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def put(self, request, pk=None, *args, **kwargs):
        """Method to handle PUT Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = SentenceSerializer(request.user, data=request.data, partial=False)
            if serializer.is_valid():
                try:
                    result_data = Sentence.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update Sentence object and save it to DB.")
                    logger.warning(f"{ex}: Could not update Sentence object and save it to DB.")

        return Response(self.build_response(status_code, result_data), status=status_code)

    def patch(self, request, pk=None, *args, **kwargs):
        """Method to handle PATCH Request"""
        status_code = status.HTTP_400_BAD_REQUEST
        result_data = None
        if pk:
            serializer = SentenceSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                try:
                    result_data = Sentence.objects.filter(pk=pk).update(**request.data)
                    status_code = status.HTTP_200_OK
                except Exception as ex:
                    print(f"{ex}: Could not update Sentence object and save it to DB.")
                    logger.warning(f"{ex}: Could not update Sentence object and save it to DB.")

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
                logger.warning(f"{ex}: Could not delete Sentence object with ID: {pk}")

        return Response(self.build_response(status_code, result_data), status=status_code)
