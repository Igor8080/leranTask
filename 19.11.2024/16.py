a = float(input("Введите действительное число a: "))
if a <= 0:
    f = 0
elif 0 < a <= 1:
    f = a
else:
    f = a**2
print("f(a) =", f)