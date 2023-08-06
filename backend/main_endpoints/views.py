from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnswerSerializer
from utils.FileHandler import FileHandler
from django.conf import settings
import pickle
import numpy as np
from ML.ChatBot import ChatBot
import tensorflow as tf
from keras.preprocessing import image
import keras.utils as image


@api_view(["POST"])
def survey(request):
    answers = request.data
    if not isinstance(answers, list):
        return Response(
            {"message": "Invalid data type,must be a list"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if len(answers) != 22:
        return Response(
            {"message": "Invalid number of answers"}, status=status.HTTP_400_BAD_REQUEST
        )
    for answer in answers:
        serializer = AnswerSerializer(data=answer)
        serializer.is_valid(raise_exception=True)

    encoded_answers = [1 if answer["answer"] == "Yes" else 0 for answer in answers] * 6

    encoded_answers = np.array(encoded_answers).reshape(1, -1)
    predictor = pickle.load(open("ML/random_forest.pkl", "rb"))
    res = predictor.predict(encoded_answers)
    return Response({"prediction": res}, status=status.HTTP_200_OK)


@api_view(["POST"])
def upload(request):
    file = request.data.get("file")

    file_type = file.content_type.split("/")[1]
    handler = FileHandler(file, f"{settings.MEDIA_ROOT}/uploaded_file.{file_type}")
    handler.create_temp_file()

    input_shape = (64, 64, 3)
    cnn = tf.keras.models.Sequential()
    cnn.add(
        tf.keras.layers.Conv2D(
            filters=32, kernel_size=3, activation="relu", input_shape=input_shape
        )
    )
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    cnn.add(tf.keras.layers.Flatten())
    cnn.add(tf.keras.layers.Dense(units=128, activation="relu"))
    cnn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

    # Load the model weights from the HDF5 file
    cnn.load_weights("ML/cnn_model.h5")

    # Compile the model
    cnn.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    modified_image = image.load_img(
        f"{settings.MEDIA_ROOT}/uploaded_file.{file_type}", target_size=(64, 64)
    )
    modified_image = image.img_to_array(modified_image)
    modified_image = np.expand_dims(modified_image, axis=0)

    result = cnn.predict(modified_image)
    if result[0][0] == 0:
        prediction = "Negative (normal)"
    else:
        prediction = "Positive (Covid)"
        
    # ML upload Model comes here
    handler.delete_file()
    return Response({"result": prediction}, status=status.HTTP_200_OK)


@api_view(["POST"])
def chat_bot(request):
    question = request.data.get("question")

    # ML chatbot Model comes here
    ans = ChatBot().predict(question)

    # Substitue thie dictionary with the ML model response
    return Response({"message": ans}, status=status.HTTP_200_OK)


# @api_view(["POST"])
# def heart(request):
#     answers = request.data
#     if not isinstance(answers, list):
#         return Response(
#             {"message": "Invalid data type,must be a list"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
#     if len(answers) != 13:
#         return Response(
#             {"message": "Invalid number of answers"}, status=status.HTTP_400_BAD_REQUEST
#         )
#     for answer in answers:
#         serializer = AnswerSerializer(data=answer)
#         serializer.is_valid(raise_exception=True)

#     encoded_answers = [
#         1 if answer["answer"] == "Yes" else 0 for answer in answers
#     ]*6

#     encoded_answers = np.array(encoded_answers).reshape(1, -1)
#     predictor = pickle.load(open("ML/random_forest.pkl", "rb"))
#     res = predictor.predict(encoded_answers)
#     return Response({"prediction": res}, status=status.HTTP_200_OK)
