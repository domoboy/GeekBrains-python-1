# GeekBrains-python-1
HomeTask for the course python-1

Lesson 1, normal
-----------------
* Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
* Задача-2: Исходные значения двух переменных запросить у пользователя. Поменять значения переменных местами. Вывести новые значения на экран.Решите задачу используя только две переменные
* Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0. Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
```python
import math
math.sqrt(4) - вычисляет корень числа 4
```
Lesson 1, hard
-----------------
* Задание-1:
 Ваня набрал несколько операций в интерпретаторе и получал результаты:
```python
a == a**2
True
a == a*2
True
a > 999999
True
```
Вопрос: Чему была равна переменная a, если точно известно что её значение не изменялось?
Lesson 2, normal
-----------------
* Задание-1:
 Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут
 квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
 если такой корень вообще можно извлечь
 Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

* Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
 Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
 Склонением пренебречь (2000 года, 2010 года)

* Задача-3: Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100
 В списке должно быть n - элементов
 Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random

* Задача-4: Дан список заполненный произвольными целыми числами
 Получите новый список, элементами которого будут только уникальные элементы исходного
 
 
Lesson 2, hard
----------------- 
* Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
 Определить координату y, точки с заданной координатой x
```python
equation = 'y = -12x + 11111140.2121'
x = 2.5
```
 вычислите и выведите y

* Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
 Условия коррекности:
 - День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
 - Месяц должен приводиться к целому числу в диапазоне от 1 до 12
 - Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
 - Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

 Пример корректной даты
```python
date = '01.11.1985'
```
 Примеры некорректных дат
```python
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'
```
* Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
 Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
 Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
 на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
```python
         ...
     12  13  14
     9   10  11
     6   7   8
       4   5
       2   3
         1
 ```
  Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
  на каком этаже она находится и какая она по счету слева на этом этаже.
  Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
  Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
 Пример:
 ```python
 Вход: 13
 Выход: 6 2

 Вход: 11
 Выход: 5 3
```
Lesson 3, normal
-----------------
* Задание-1:
 Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
 Первыми элементами ряда считать цифры 1 1
```python
def fibonacci(n, m):
    pass
```
* Задача-2:
 Напишите функцию сортирующую принимаемый список по возрастанию.
 Для сортировки используйте любой алгоритм (например пузырьковый).
 Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()
```python
def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
```
* Задача-3:
 Напишите собственную реализацию функции filter
 Разумеется, внутри нельзя использовать саму функцию filter


* Задача-4:
 Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
 Определить, будут ли они вершинами параллелограмма
