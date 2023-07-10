def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


def count(array, element):
    _cnt = 0
    for i, a in enumerate(array):
        if a == element:
            _cnt += 1
    return _cnt


# array = list(map(int, input('Array=').split()))
array = list(map(int, '1 4 8 6 3 5 5 6 45 6'.split()))
# element = int(input('Element='))
element = 6
print('Found in position =',find(array, element))
print('Found ',count(array, element), 'times.')


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит, элемент отсутствует
    
    middle = (right + left) // 2  # находим середину
    print('Middle =', middle, end='. ')
    try:
        if array[middle] == element:  # если элемент в середине
            print('\nFound =', middle)
            return middle  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            print(' Look left.')
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            print(' Look right.')
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return False


element = 17
array = [i for i in range(1, 100)]  # 1,2,3,4,...
array[16] = 16

# запускаем алгоритм на левой и правой границе
print('\nArray =', array, 'Element =', element)
print('Result is ', binary_search(array, element, 0, 99), '.')
