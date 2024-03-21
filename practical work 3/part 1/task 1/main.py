print ("Введите х")
x = float(input())

print ("Введите y")
y = float(input())

x6y = x + 6 * y
delxy = x / y
sumxy = x + y
x3y = x + 3 *y


max = max(sumxy, x3y)
min = min(x6y, delxy)

u = min / max
print(u)