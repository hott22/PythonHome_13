class ImpossibleTriangleException(BaseException):
    def __str__(self):
        return 'Одна из сторон треугольника не должна превышать сумму двух других'

