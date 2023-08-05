from django.urls import path
from .views import survey


urlpatterns = [
    path("survey/", survey, name="survey"),
]
