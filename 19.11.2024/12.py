sequence = list(map(int, input("Введите последовательность чисел: ").split()))
for i in range(1, len(sequence) - 1):
    if sequence[i] > sequence[i - 1] and sequence[i] > sequence[i + 1] and sequence[i] % 2 == 0:
        print("Четный локальный максимум найден")
        break
else:
    print("Четный локальный максимум не найден")