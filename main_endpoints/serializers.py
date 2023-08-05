from rest_framework.serializers import ModelSerializer, CharField
from main_endpoints.models import Answer


class AnswerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Answer
