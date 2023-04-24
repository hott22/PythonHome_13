class NegativeValueException(BaseException):
    def __str__(self):
        return f'Значение стороны треугольника не должна быть меньше 1.'
