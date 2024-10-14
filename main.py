# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()  # Все параметры по умолчанию
print_params(b=25)  # Только аргумент b изменён
print_params(c=[1, 2, 3])  # Только аргумент c изменён

# Создание списка и словаря для распаковки
values_list = [42, 'hello', False]
values_dict = {'a': 3.14, 'b': 'слово', 'c': None}

# Передача параметров с помощью распаковки
print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

# Комбинация распаковки и отдельных параметров
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка двух элементов из списка и отдельный параметр
