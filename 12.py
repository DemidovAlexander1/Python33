num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)
