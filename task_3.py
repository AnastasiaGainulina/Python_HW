# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

a = int(input('Напишите число: '))

def fib_gen():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

fs = fib_gen()
next(fs)
for i in range(a):
    print(next(fs))
