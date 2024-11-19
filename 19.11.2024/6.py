x = float(input("Введите действительное число: "))
choice = int(input("Введите номер действия (1-4): "))
if choice == 1:
    print(x ** 2)
elif choice == 2:
    print(x ** 0.5)
elif choice == 3:
    print(math.sin(x))
elif choice == 4:
    print(math.cos(x))
else:
    print("Неверный выбор")