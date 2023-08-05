from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnswerSerializer
from utils.FileHandler import FileHandler
from django.conf import settings


@api_view(["POST"])
def survey(request):
    answers = request.data
    if not isinstance(answers, list):
        return Response(
            {"message": "Invalid data type,must be a list"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if len(answers) < 20 or len(answers) > 20:
        return Response(
            {"message": "Invalid number of answers"}, status=status.HTTP_400_BAD_REQUEST
        )
    for answer in answers:
        serializer = AnswerSerializer(data=answer)
        serializer.is_valid(raise_exception=True)

    # ML survey Model comes here
    encoded_answers = [
        111111 if answer["answer"] == "Yes" else 000000 for answer in answers
    ]

    # survey_model(encoded_answers)

    # Substitue thie dictionary with the ML model response
    return Response({"message": "hello world"}, status=status.HTTP_200_OK)


@api_view(["POST"])
def upload(request):
    file = request.data.get("file")

    file_type = file.content_type.split("/")[1]
    handler = FileHandler(file, f"{settings.MEDIA_ROOT}/uploaded_file.{file_type}")
    handler.create_temp_file()

    # ML upload Model comes here

    handler.delete_file()
    return Response({"message": "hello world"}, status=status.HTTP_200_OK)


@api_view(["POST"])
def chat_bot(request):
    question = request.data.get("question")

    # ML chatbot Model comes here

    # Substitue thie dictionary with the ML model response
    return Response({"message": "hello world"}, status=status.HTTP_200_OK)