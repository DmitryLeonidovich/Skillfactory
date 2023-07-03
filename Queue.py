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
        self.empty = False
        self.tail += 1
        if self.tail == self.max_size:
            self.tail = 0
        return True
    
    def pop(self):
        if self.empty:
            return None
        d_pop = self.tasks[self.head]
        self.head += 1
        self.empty = self.head == self.tail
        if self.head == self.max_size:
            self.head = 0
        if self.head == self.tail:
            self.empty = True
            self.size()
        return d_pop
    
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
            # print('H=', head, 'T=', self.tail)
            out_list.append(self.tasks[head])
            head += 1
            if head == self.max_size:
                head = 0
            done = not head == self.tail
        return out_list
    
    def size(self):
        if self.tail == self.head:
            if self.empty:
                sz = 0
            else:
                sz = self.max_size
        elif self.tail < self.head:
            sz = self.max_size + self.tail - self.head
        elif self.tail > self.head:
            sz = self.tail - self.head
        return sz

# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)
while True:
    # q.show_all()
    print(q.show())
    # print('H=', q.head, 'T=', q.tail, "Empty=", q.empty)
    cmd = (input("Введите команду:").split())
    
    if cmd[0] == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
            
    elif cmd[0] == "size":
        print("Количество задач в очереди:", q.size())
        
    elif len(cmd) > 1 and cmd[0] == "push":
        if q.size() != q.max_size:
            d = cmd[1]
            # d = input("Введите данные:")
            if q.push(d):
                print("Успешно добавлено=", d)
            else:
                print('Добавить', d, 'не удалось...')
        else:
            print("Очередь переполнена")
    
    elif cmd[0] == "push":
        if q.size() != q.max_size:
            d = input("Введите данные:")
            if q.push(d):
                print("Успешно добавлено=", d)
            else:
                print('Добавить', d, 'не удалось...')
        else:
            print("Очередь переполнена")
    
    elif cmd[0] == "pop":
        d = q.pop()
        if d == None:
            print("Очередь пустая")
        else:
            print('Извлечено=', d)
            
    elif cmd[0] == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
            
    elif cmd[0] == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
            
    elif cmd[0] == "exit":
        for _ in range(q.size()):
            q.do()
            
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")