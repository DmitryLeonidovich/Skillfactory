step = 0

def p0(n):
    global step
    step += 1
    if n == 0:
        return
    else:
        p0(n-1)
        print('Step=', step, n)
    return
p0(5)
print("*" * 50)
step = 0
def p1(val):
    global step
    step += 1
    if val == 0:
        return
    else:
        val -= 1
        print('Step_1 =', step, '=', val)
        p1(val)
        print('Step_2 =', step, '=', val)
    return
p1(8)
print("*" * 50)
step = 0
load = 0
def p2(val):
    global step, load
    step += 1
    if val == 0:
        return
    else:
        load += 1
        print('Step_1 =', step, '=', val, 'Load_1 =', load)
        p2(val-1)
        load += 1
        print('Step_2 =', step, '=', val, 'Load_2 =', load)
    return
p2(8)


def par_checker(string):
    stack = []  # инициализируем стек
    
    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
            print(stack)
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем,
            # пуст ли стек и является ли верхний элемент открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
                print(stack)
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0

print(par_checker("((()))"))
