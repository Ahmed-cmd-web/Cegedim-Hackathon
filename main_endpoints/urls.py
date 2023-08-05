from django.urls import path
from .views import survey, upload, chat_bot


urlpatterns = [
    path("survey/", survey, name="survey"),
    path("upload/", upload, name="upload"),
    path("chat_bot/", chat_bot, name="chat_bot"),
]
