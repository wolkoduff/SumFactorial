n = int(input())
summa = 0
factorial = 1
i = 1

while n >= 1:
    factorial *= i
    summa += i/factorial
    i += 1
    n -= 1

print(summa)
