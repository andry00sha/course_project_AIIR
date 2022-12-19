from django.shortcuts import render
import numpy as np
from rest_framework.response import Response
from rest_framework.views import APIView

from func_app.func import degree
from .models import MatrixDegree
from .serializers import MatrixSerializer


class DegreeView(APIView):

    def get(self, request, matrix, step):
        degree1 = MatrixDegree(matrix, step, degree(matrix, step))

        serializer_for_request = MatrixSerializer(instance=degree1).data

        return Response(serializer_for_request)
# Create your views here.
