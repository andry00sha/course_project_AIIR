import numpy as np


def degree(matrix: str, step: int):
    # Разбиваем строку matrix на элементы матрицы
    elements = matrix.split('-')
    # Преобразуем элементы в числа и сохраняем в матрицу numpy
    matrix = np.array([[int(x) for x in row.split('_')] for row in elements])

    # Вычисляем матрицу matrix в степени step

    result = np.linalg.matrix_power(matrix, step)


    # Формируем ответ в виде текста



    return(result)