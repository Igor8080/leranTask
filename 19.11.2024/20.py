x, y, z = map(float, input("Введите три действительных числа: ").split())
if x + y + z < 1:
    if x < y and x < z:
        x = (y + z) / 2
    elif y < x and y < z:
        y = (x + z) / 2
    else:
        z = (x + y) / 2
else:
    if x < y:
        x = (y + z) / 2
    else:
        y = (x + z) / 2
print(x, y, z)