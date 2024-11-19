n = int(input("Введите количество чисел: "))
numbers = list(map(float, input("Введите числа: ").split()))
doubled_sum = 2 * sum([x for x in numbers if x > 0])
print("Удвоенная сумма положительных элементов:", doubled_sum)