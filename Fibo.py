# ФУНКЦИЯ - ГЕНЕРАТОР
# ЧИСЛА ФИБОНАЧЧИ
# ---------------------------------------------------------------
print('Просто ряд чисел Фибоначчи')
a, b = 0, 1
for i in range(0,21):
    print(a, end=' ')
    a, b = b, a + b
print('Done\n')
# ---------------------------------------------------------------
def fib_v1():
    def fib_next():         # вспомогательная вложенная функция.
        nonlocal a, b
        a, b = b, a + b
        return b            # возвращает вычисленное ЧФ.
    a, b = 0, 1             # начальные значения для вычисления ЧФ.
    yield a                 # возврат генератором 1-го ЧФ.
    yield b                 # возврат генератором 2-го ЧФ.
    while b < 144:
        yield fib_next()    # возврат генератором ЧФ с 3-го по 13-ое.
    yield fib_next()        # возврат генератором 14-го ЧФ.
    yield fib_next()        # возврат генератором 15-го ЧФ.

def fib_v2():
    def fib_next():         # вспомогательная вложенная функция.
        nonlocal a, b
        a, b = b, a + b
        return b            # возвращает вычисленное ЧФ.
    a, b = 0, 1             # начальные значения для вычисления ЧФ.
    yield a                 # возврат генератором 1-го ЧФ.
    yield b                 # возврат генератором 2-го ЧФ.
    while b < 144:
        yield fib_next()    # возврат генератором ЧФ с 3-го по 13-ое.
    yield fib_next()        # возврат генератором 14-го ЧФ.
    yield fib_next()        # возврат генератором 15-го ЧФ.

def fib_v3():
    def fib_next():         # вспомогательная вложенная функция.
        nonlocal a, b
        a, b = b, a + b
        return b            # возвращает вычисленное ЧФ.
    a, b = 0, 1             # начальные значения для вычисления ЧФ.
    yield a                 # возврат генератором 1-го ЧФ.
    yield b                 # возврат генератором 2-го ЧФ.
    while b < 144:
        yield fib_next()    # возврат генератором ЧФ с 3-го по 13-ое.
    yield fib_next()        # возврат генератором 14-го ЧФ.
    yield fib_next()        # возврат генератором 15-го ЧФ.

print('Ряд чисел Фибоначчи (используется функция - генератор. Внутри ограничена 15-ю числами на выдачу.)')

# Вариант 1 - работает
print('Вариант 1 - работает')
for num in fib_v1():
    print(num, end=' ')
print('Done v1')

# Вариант 2 - не работает
print('Вариант 2 - не работает')
for i in range(0,5):
    num = fib_v2()
    print(num, end=' ')
print('Done v2')

# Вариант 3 - не работает
print('Вариант 3 - не работает')
for i in range(0,10):
    print(fib_v3(), end=' ')
print('Done v3')