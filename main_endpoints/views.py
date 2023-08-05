from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnswerSerializer


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
    encoded_answers = [1 if answer["answer"] == "Yes" else 0 for answer in answers]

    # survey_model(encoded_answers)

    # Substitue thie dictionary with the ML model response
    return Response({"message": "hello world"}, status=status.HTTP_200_OK)
