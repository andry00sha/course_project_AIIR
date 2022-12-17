from django.http import HttpResponse
import numpy as np


def degree(request, size, matrix, step):

    size = request.GET.get('size', None)
    step = request.GET.get('step', None)

    if step is None:
        return HttpResponse('Степень матрицы не указана.')

    try:
        step = int(step)
    except :
        return HttpResponse('Данные введены некорректно. Степень должны быть числом')

    if step <= 0:
        return HttpResponse('Число не положительное.')

    if size is None:
        return HttpResponse('Размер матрицы не указан.')

    try:
        size = int(size)
    except :
        return HttpResponse('Данные введены некорректно. Размер матрицы должен быть числом.')

    if size <= 0:
        return HttpResponse('Число меньше, чем возможный размер матрицы.')

    matrix = request.GET.get('matrix', None)

    if matrix is None :
        return HttpResponse('Матрица не заполнена.')

    matrix = matrix.split('-')

    new_matrix = []

    if len(matrix) != size:
        return HttpResponse('Матрица неправильного размера.')

    for row in matrix:
        try:
            row = list(map(float, row.split('_')))
        except:
            return HttpResponse('В матрице есть недопустимые значения!')

        if len(row) != size :
            return HttpResponse('Неправильный размер строки в матрице')

        new_matrix.append(row)

        new_matrix = np.array(new_matrix)

        try:
            degree_matrix = np.linalg.matrix_power(new_matrix, step)
        except np.linalg.LinAlgError as e:
            return HttpResponse('Работа с матрицей невозможна из-за алгебраической ошибки.')

        for row in degree_matrix:
            for i in range(len(row)):
                row[i] = round(row[i], 3)

    degree_matrix_str = '<br/><br/>'.join(
        ['&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(map(str, row)) for row in degree_matrix])
    degree_matrix_str = '<p style=\"font-size:20pt;\">' + degree_matrix + '</p>'

    # return HttpResponse(degree_matrix_str)
    return HttpResponse(degree_matrix)
