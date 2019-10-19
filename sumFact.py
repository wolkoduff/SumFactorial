# версия через цикл while
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
 
# Версия без цикла while

n = int(input())
b = 0
factorial = 1

for i in range(1, n, 1):
    factorial *= i
    b += i / factorial

print(b)
