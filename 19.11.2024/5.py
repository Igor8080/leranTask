prev = int(input("Введите первое число: "))
while True:
    current = int(input("Введите следующее число: "))
    if current < prev:
        break
    prev = current