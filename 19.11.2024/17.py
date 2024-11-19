a = float(input("Введите действительное число a: "))
n = int(input("Введите натуральное число n: "))
result = sum([a**i for i in range(n + 1)])
print("Результат:", result)