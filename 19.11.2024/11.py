a, b, z = map(float, input("Введите целые числа a и b и действительное число z: ").split())
x = a % b
if a % b == 0:
    z *= x
else:
    z /= x
print(z)