import math

a, b, c = map(float, input("Введите коэффициенты a, b, c: ").split())
discriminant = b**2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Корни уравнения:", x1, x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("Единственный корень:", x)
else:
    print("Действительных корней нет")