num = int(input("Введите положительное целое число: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print("Сумма цифр:", sum_of_digits)