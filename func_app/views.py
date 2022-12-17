from django.http import HttpResponse
import func_app

# Create your views here.


def degree(request, size, matrix, step):
    return HttpResponse(f"Возведение матрицы {matrix} в степень {step} дает следующий результат: {func_app.degree(request, size, matrix, step)}")

