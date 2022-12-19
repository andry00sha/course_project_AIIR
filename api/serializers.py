import numpy as np
from rest_framework import serializers
from func_app.func import degree
from .models import MatrixDegree


class MatrixSerializer(serializers.Serializer):
    matrix = serializers.CharField()
    step = serializers.IntegerField()
    result = serializers.CharField()

