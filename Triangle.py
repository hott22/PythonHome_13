from home13.ImpossibleTriangleException import ImpossibleTriangleException
from home13.NegativeValueException import NegativeValueException


class Triangle:
    def __init__(self, first: int, second: int, third: int):
        if first < 1 or second < 1 or third < 1:
            raise NegativeValueException
        elif first + second <= third or first + third <= second or second + third <= first:
            raise ImpossibleTriangleException
        else:
            self.first = first
            self.second = second
            self.third = third

    def __str__(self):
        return f'Треугольник со сторонами: {self.first}, {self.second}, {self.third}'



if __name__ == '__main__':
    a = Triangle(2, 5, 7)
    print(a)

