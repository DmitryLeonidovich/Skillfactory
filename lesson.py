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


# Создадим класс Queue — нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи
        
        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди
        self.empty = True  # флаг пустой очереди
    
    # !!! Класс далее нужно дополнить методами !!!
    def is_empty(self):
        return self.tail == self.head and self.empty
    
    def push(self, data):
        if self.tail == self.head and not self.empty:
            return False  # очередь заполнена
        self.tasks[self.tail] = data
        self.tail += 1
        if self.tail == self.max_size:
            self.tail = 0
        return True
    
    def pop(self):
        if self.empty:
            return None
        d = self.tasks[self.head]
        self.empty = self.head == self.tail
        if not self.empty:
            self.head += 1
            if self.head == self.max_size:
                self.head = 0
        return d
    
    def show_all(self):
        for i in self.tasks:
            print(i, end=" ")
        print()
    
    def show(self):
        out_list = []
        if self.is_empty():
            return out_list
        head = self.head
        done = True
        while done:
            out_list.append(self.tasks[head])
            done = not head == self.tail - 1
            if head == self.max_size:
                head = 0
            else:
                head += 1
        return out_list
    
    def size(self):
        sz = self.tail - self.head
        if self.tail < self.head:
            sz += self.max_size
        elif self.tail > self.head:
            pass
        elif sz == self.empty:
            sz = self.max_size
        return sz

# Используем класс
# size = int(input("Определите размер очереди: "))
q = Queue(2)
q.push("1-")
q.push("2-")
while True:
    q.show_all()
    print(q.show())
    cmd = input("Введите команду:")
    
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
            
    elif cmd == "size":
        print("Количество задач в очереди:", q.size(), 'H=', q.head, 'T=', q.tail)
    elif cmd == "push":
        if q.size() != q.max_size:
            d = input("Введите данные:")
            if q.push(d):
                print("Успешно добавлено=", d)
            else:
                print('Добавить', d, 'не удалось...')
        else:
            print("Очередь переполнена")
            
    elif cmd == "pop":
        d = q.pop()
        if d == None:
            print("Очередь пустая")
        else:
            print('Извлечено=', d)
            
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
            
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
            
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
            
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")