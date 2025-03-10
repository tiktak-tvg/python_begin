# Условная функция if
##### Синтаксис инструкции.
- Оператор-выражение ``if``

![image](https://github.com/tvgVita69/python_begin/assets/98489171/6d372d9f-fa6f-4bba-af2b-f7810601af71)

- Оператор-выражение ``if-else``

![image](https://github.com/tvgVita69/python_begin/assets/98489171/07a93b02-97eb-4ca8-a30c-b6a6f25b84f5)

- Оператор-выражение ``if-elif-else``

![image](https://github.com/tvgVita69/python_begin/assets/98489171/f3f37702-6fb2-4930-9e79-3759c73e9c6e)

Варианты действий ``elif``
```
if <условие 1>:
<действия 1>
elif <условие 2>:
<действия 2>
elif <условие 3>:
<действия 3>
elif ...:
...
elif <условие n>:
<действия n>
else:
<действия (n + 1)>
```

![image](https://github.com/tvgVita69/python_begin/assets/98489171/af9387ee-c975-4d05-bb12-9bfb1c90d296)

```
num = 11
if num > 10:
    print("Число больше 10")
```

```
num = 9
if num > 10:
    print("Число больше 10")
else
    print("Число меньше 10")
```

```
num = 10
if num > 10:
    print("Число больше 10")
elif num < 10:
    print("Число меньше 10")
else:
    print("Число равно 10")
```

![image](https://github.com/tvgVita69/python_begin/assets/98489171/a34b8b95-d83d-4d10-b9b2-9d1cfb52e646)

##### Можно использовать и тернарные выражения.
```
>>> num = 10
>>> a = print('Число больше 10') if num > 10 else print('Число меньше 10') if num < 10 else print("Число равно 10")
Число равно 10
>>> num = 11
>>> a = print('Число больше 10') if num > 10 else print('Число меньше 10') if num < 10 else print("Число равно 10")
Число больше 10
>>> num = 1
>>> a = print('Число больше 10') if num > 10 else print('Число меньше 10') if num < 10 else print("Число равно 10")
Число меньше 10
>>>
```

![image](https://github.com/tvgVita69/python_begin/assets/98489171/b796a1e4-e338-4acc-bf91-f215d96c270b)

```
print('hello' if len('xy') == 2 else 'bye')
hello
print('hello' if len('x') == 2 else 'bye')
bye
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/93880ef0-b9b4-4520-afc5-1759e99fdda8)

##### Тернарные операторы наиболее широко известны в Python как условные выражения. Эти операторы возвращают что-то взависимости от того, является ли условие истиной или ложью. Они стали частью языка с версии 2.4.
> Шаблоны и примеры использования: ``condition_if_true if condition else condition_if_false.``

> Пример:

```
is_good = True
state = "good" if is_good else "not good"
```
Такой подход позволяет быстро проверить условие, а не писать несколько строчек оператора ``if``. Зачастую это очень удобно,поскольку позволяет писать более компактный код, сохраняя его читабельность. Другим вариантом (менее очевидным и не настолько широко распространенным) является использование кортежей. 
> Вот пример кода:
``(if_test_is_false, if_test_is_true)[test]``
> Пример:
```
good = True
personality = ("вредная", "добрая")[good]
print("Кошка ", personality)
Вывод:
Кошка добрая
```
Данная конструкция работает поскольку в Python ``True == 1`` и ``False == 0``. Помимо кортежей можно использовать списки. Пример выше редко используется и в основном считается плохой практикой у разработчиков, поскольку не является в должной мере "питонистичным" решением. Вдобавок здесь легко ошибиться в последовательности значений в кортеже. Другой причиной не пользоваться тернарным оператором на кортежах является обработка всего кортежа при исполнении, когдакак для ``if-else`` оператора такого не происходит.

> Пример:
```
condition = True
print(2 if condition else 1/0)
```
Вывод: 2
``print((1/0, 2)[condition])``
- Вывод: Было вызвано исключение ZeroDivisionError

Во втором примере сначала собирается кортеж, а затем находится элемент под заданным индексом. Тернарный оператор на ``if-else`` следует обычной логике условного оператора ``if``. Таким образом, если один из случаев может вернуть ошибку илиобработка обоих случаев является слишком затратной операцией, то вариант с кортежами точно не стоит использовать.
##### Сокращенный тернарный оператор.
В Python также существует более краткий вариант тернарного оператора.<br>
Этот синтакcис был добавлен в Python 2.5 и может быть использован в новых версиях.

> Пример:

``True or "Some"``
> **Вывод:True**<br>
``False or "Some"``<br>
> **Вывод:'Some'**

Первое выражение ``(True or "Some")`` возвращаетTrueи второе - ``Some``.

Это удобно, когда нужно быстро проверить вернувшееся из функции значение и показать сообщение, если значения не было(вернулся None):
```
func_output = None
msg = func_output or "Не было возвращено данных"
print(msg)
Вывод:
>?Не было возвращено данных
```

##### Применение ``input()``
> Например введём ``тернарные условные операторы``:

```
Пример 1.
text = input()
if "ернар" in text:
    print("Встретилось 'ернар' в предложении: ", text)
else:
    print("'тернар' не найдено.")

>?тернарные условные операторы
Встретилось 'ернар' в предложении:  тернарные условные операторы

Пример 2.
text = input()
if "Встрет" in text:
    print("Встретилось 'Встрет' в предложении: ", text)
else:
    print("'Встрет' не найдено.")

>?тернарные условные операторы 
'Встрет' не найдено.
```

##### В Python нет встроенного оператора ``switch/case``. Вместо этого приходится использовать условный оператор ``if``.

> Такой код как наример в C#
```
switch (day) {
    case "Понедельник":
        System.out.println("Первый день недели.");
        break;
    case "Tuesday":
        System.out.println("Второй день недели.");
        break;
    // и так далее
    default:
        System.out.println("Неизвестный день");
}
```

> В Python заменяется таким 

```
Пример 1.
day = 'Вторник'
if day == "Понедельник":
    print("Первый день недели.")
elif day == "Вторник":
    print("Второй день недели.")
elif day == "Вторник":
    print("Третий день недели.")
elif day == "Среда":
    print("Четвертый день недели.")
elif day == "Четверг":
    print("Пятый день недели.")
elif day == "Пятница":
    print("Шестой день недели.")
elif day == "Суббота":
    print("Седьмой день недели.")
elif day == "Воскресенье":
    print("Второй день недели.")
else:
    print("Неизвестный день")
Второй день недели.

Пример 2.
day = 'Суббота'
if day == "Понедельник":
    print("Первый день недели.")
elif day == "Вторник":
    print("Второй день недели.")
elif day == "Вторник":
    print("Третий день недели.")
elif day == "Среда":
    print("Четвертый день недели.")
elif day == "Четверг":
    print("Пятый день недели.")
elif day == "Пятница":
    print("Шестой день недели.")
elif day == "Суббота":
    print("Седьмой день недели.")
elif day == "Воскресенье":
    print("Второй день недели.")
else:
    print("Неизвестный день")
Седьмой день недели.
```
> Или как альтернативу оператору switch/case — использование словарей.

```
def monday():
    return "Второй день недели."
def tuesday():
    return "Третий день недели."
def wednesday():
    return "Четвертый день недели."
def thursday():
    return "Пятый день недели."
def friday():
    return "Шестой день недели."
def saturday():
    return "Седьмой день недели."
def sunday():
    return "Первый день недели."
def default():
    return "Неизвестный день"
switch = {
    "Понедельник": monday,
    "Вторник": tuesday,
    "Среда": wednesday,
    "Четверг": thursday,
    "Пятница": friday,
    "Суббота": saturday,
    "Воскресенье": sunday
}
# использование словаря
print(switch.get(day, default)())
Седьмой день недели.
```
##### Вложенные конструкции.

Любое количество блоков ``if…elif…else`` можно разместить внутри другого оператора ``if…elif…else``
> Например:
- Оператор if внутри другого if-оператора

![image](https://github.com/tvgVita69/python_begin/assets/98489171/69a14337-d69f-4067-8220-47272003ab89)

```
num = float(input("Введите число: "))
if num >= 0:
    if num == 0:
        print("0")
    else:
        print("Положительное число")
else:
    print("Отрицательное число")
Введите число: >? 5
Положительное число

num = float(input("Введите число: "))
if num >= 0:
    if num == 0:
        print("0")
    else:
        print("Положительное число")
else:
    print("Отрицательное число")
Введите число: >? -1
Отрицательное число

num = float(input("Введите число: "))
if num >= 0:
    if num == 0:
        print("0")
    else:
        print("Положительное число")
else:
    print("Отрицательное число")
Введите число: >? 0
0
```
или в одну строку
```
>>> a = 55
>>> b = f'{a} < 50' if a < 50 else (f'{a} > 60' if a > 60 else f'50 > {a} < 60')
>>> print(b)
50 > 55 < 60
>>> a = 45
>>> b = f'{a} < 50' if a < 50 else (f'{a} > 60' if a > 60 else f'50 > {a} < 60')
>>> print(b)
45 < 50
>>> a = 65
>>> b = f'{a} < 50' if a < 50 else (f'{a} > 60' if a > 60 else f'50 > {a} < 60')
>>> print(b)
65 > 60
>>>
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/60e1298a-4c5a-4830-83ed-119c1b4c054f)

> Другой пример:
- Оператор if-else внутри условия else

 ![image](https://github.com/tvgVita69/python_begin/assets/98489171/460a762b-ff8b-4c43-ab74-8d5cdb5e20f0)
 
```
x = 5
if x > 7:
    print("x больше 7")
else:
    print("x не больше 7")
    if x % 2 == 0:
        print("x - четное число")
    else:
        print("x - нечетное число")
```
##### Условный оператор с bool
>- Результат выполнения логических операций с операторами ``and``, ``or``.<br>

1. **and**

![image](https://github.com/tvgVita69/python_begin/assets/98489171/ec814c39-12b4-4c4d-8bbc-69424c2c1389)

- то есть результат будет истинным ``(True)`` только в случае, когда оба простых условия ``С1`` и ``С2`` истинны<br>

2. **or**
  
![image](https://github.com/tvgVita69/python_begin/assets/98489171/3149f342-71c3-47ae-adf4-ea4a0cdf8c8b)

- то есть результат будет истинным в случае, когда хотя бы одно простое условие является истинным.<br>

>- Результат выполнения логической операции с оператором ``not`` над условием ``С`` определяется так:

![image](https://github.com/tvgVita69/python_begin/assets/98489171/906ea5b7-097d-4ef9-82b9-c02fa0fcf2c3)

- то есть он противоположен значению условия ``С``.

При проверке сложного условия сначала выполняются операции сравнения ``(<, <=, >, >=, ==, !=)``, а затем – логические операции в таком порядке:<br> 
сначала все операции с оператором ``not``, затем – с оператором ``and``, и в самом конце – с оператором ``or`` (во всех случаях – слева направо).<br> 
Для изменения порядка действий используют круглые скобки.<br>

Иногда условия получаются достаточно длинными, и их хочется перенести на следующую строку. Сделать это в Python можно двумя способами:
- использовать обратный слэш («\»):
```
if v < 400 and v != 2 and v != 3 and v != 12 and \
v != 13 and v != 22 and v != 23:
...

```
- взять все условие в скобки (перенос внутри скобок разрешен):
```
if (v < 400 and v != 2 and v != 3 and v != 12 and v != 13
and v != 22 and v != 23):
...
```
> Рассмотрим примеры:

```
x = True
if x is True:
    print("True")
else:
    print("False")

y = False
if y is True:
    print('True')
else:
    print('False')
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/21f30ff0-1ca3-49ed-b15b-50f8b757e1eb)

```
z = False
if z is False:
    print('z = False')
    z = False
    if not z:
        print('Переменная z хранит ложное значение')
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/0abc0464-14a5-4ffc-85a8-78bd5d7c8505)

##### Ложные значения в Python. Константы, определенные как ложные: ``None`` и ``False``. ``0(ноль)`` любого числового типа
> пустые последовательности и коллекции:
- ``""``(пустая строка),
- ``()``(пустой кортеж),
- ``[]`` (пустой список),
- ``{}``(пустой словарь),
- ``set()``(пустой набор),
- ``range(0)``(пустой диапазон).

> Например

```
a = 'Hello'
b = 'VIP client!'
c = ''
d = 0
if a:
    print(a)

if ['a', 'b']:
    print(a,b)

if not a:
    print(a)

if c:
    print(c)

if d:
    print(d)
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/094cfe24-e622-42c8-9e24-6a681fc75328)

```
if True and True:
    print('True')

if True and False:
    print('False')

# --------------------------------

if True or False:
    print('True')

if False or False:
    print('False')
```
> Результат такой

![image](https://github.com/tvgVita69/python_begin/assets/98489171/b832d477-7784-4d0b-a550-7c898f90c4fb)

```
a = 1
b = 3
c = 7

if a == 1 and b == 3 and c == 7:    # and все условия должны быть соблюдены
    print('Все условия в операторе if соблюдены')
else:
    print('Не все условия в операторе if выполнены')

# --------------------------------------------

if a == 10 and b == 3 and c == 7:     # and все условия должны быть соблюдены
    print('Все условия в операторе if соблюдены')
else:
    print('Одно или несколько условий в операторе if не соблюдены')

# --------------------------------------------

if a == 5 or b == 3 or c == 7:      # or если хоть одно условие будет соблюдено, условие выполнится
    print('Выполняется одно или несколько условий в операторе if.')
else:
    print('Ни одно из условий в операторе if не выполнено')
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/c1b74965-da33-427a-9c92-a31ea6cd2568)

##### Использования функции ``all()``

```
a = 1
b = 3
c = 7
if all([a > 0, b > 0, c > 0]):
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')

a = -1
b = 3
c = 7
if all([a > 0, b > 0, c > 0]):
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/2673cc49-f0af-49fc-a1a2-73da4bbb5111)

##### Использования функции ``any()``
```
a = 1
b = 3
c = 7
if any([a > 0, b > 0, c > 0]):
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')

a = -1
b = 3
c = 7
if any([a > 0, b > 0, c > 0]):
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/932c01e4-dd9e-447c-8810-fb8f3f957aec)

##### Комбинирование ``and`` и ``or``

```
a = 1
b = 3
c = 7
if (a > 0 and b > 0) or c > 0:
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')

a = 1
b = 3
c = 7
if (a > 0 and b > 0) or c > 10:
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')
    
a = 1
b = 3
c = 7
if (a > 10 and b > 0) or c > 0:
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')
    
a = 1
b = 3
c = 7
if (a > 10 and b > 0) or c > 10:
    print('Все условия соблюдены')
else:
    print('Не все условия соблюдены')
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/99cd4246-ca05-48fb-86da-4c1140cee29b)

