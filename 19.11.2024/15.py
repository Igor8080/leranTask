n = int(input("Введите количество чисел: "))
numbers = list(map(int, input("Введите числа: ").split()))
product = 1
for x in numbers:
    if x % 7 == 0:
        product *= x
print("Произведение элементов, кратных 7:", product)