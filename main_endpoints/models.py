from django.db import models
from django.core.validators import MinValueValidator

choices = [
    ("Yes", 1),
    ("No", 0),
]


class Answer(models.Model):
    answer = models.CharField(max_length=3, choices=choices)
    question = models.IntegerField(validators=[MinValueValidator(1)])
