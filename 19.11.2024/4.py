python
Copy
a, b, c = map(float, input("Введите три действительных числа: ").split())
result = [x for x in (a, b, c) if 1 < x < 3]
print(result)