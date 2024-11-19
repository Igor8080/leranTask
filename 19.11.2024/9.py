a, b, c, d = map(float, input("Введите четыре действительных числа: ").split())
if a <= b <= c <= d:
    a, b, c, d = max(a, b, c, d), max(a, b, c, d), max(a, b, c, d), max(a, b, c, d)
elif a > b > c > d:
    pass
else:
    a, b, c, d = a**2, b**2, c**2, d**2
print(a, b, c, d)