# Любой из параметров среза можно пропускать
# (при условии соблюдения правильной расстановки двоеточий).
# Значение по умолчанию для начала списка – 0,
# конца списка – длина списка, шага – 1.

# Создание списка чисел
my_list = [5, 7, 9, 1, 1, 2]

# Вывод элементов списка от второго (третьего) значения до конца списка
print(my_list[2:])
# Вывод всех элементов списка от начала до предпоследнего элемента
print(my_list[:-2])
# Вывод всех элементов списка в обратном порядке
print(my_list[::-1])


# Можно получить группу элементов по их индексам.
# Эта операция называется срезом списка (list slicing).

# Создание списка чисел
my_list = [5, 7, 9, 1, 1, 2]

# Получение среза списка от нулевого (первого) элемента (включая его)
# до третьего (четвёртого) (не включая)
sub_list = my_list[0:3]
# Вывод полученного списка
print(sub_list)

# Вывод элементов списка от второго до предпоследнего
print(my_list[2:-2])
# Вывод элементов списка от четвёртого (пятого) до пятого (шестого)
print(my_list[4:5])
