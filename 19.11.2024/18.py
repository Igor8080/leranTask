i, n = map(int, input("Введите i и n: ").split())
numbers = list(map(float, input("Введите числа: ").split()))
average = sum(numbers[:i] + numbers[i+1:]) / (n - 1)
print("Среднее арифметическое:", average)