# Считает все целые числа от m до n
m = int(input())
n = int(input())
for i in range(m, n+1):
    print(i)

# Выводит таблицу умножения на n (от 1 до 10)
num = int(input())
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Выводит целые числа от m до n с учетом условий
m = int(input())
n = int(input())
for i in range(m, n + 1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 15 == 0):
        print(i)

# Выводит числа от m о n в порядке убывания
m = int(input())
n = int(input())
for i in range(m , n -1, -1):
    if i % 2 != 0:
        print(i)

# Выводит числа от m до n включительно в порядке возрастания
# Или в порядке убывания

m = int(input())
n = int(input())
if m <= n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)