from django.http import HttpResponse

from func_app.func import degree


# Create your views here.


def index(request, matrix, step):
    a = str(degree(matrix, step))
    return HttpResponse(f"Возведение матрицы {matrix} в степень {step} дает следующий результат: {a}")


