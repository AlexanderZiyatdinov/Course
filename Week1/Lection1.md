# Введение

## Язык программирования Python

В этом курсе вы познакомитесь с основами программирования на языке Python (также распространены названия Пайтон и Питон, но мы не будем их использовать). Python был создан в 1991 году нидерландским программистом [Гвидо ван Россумом](https://ru.wikipedia.org/wiki/Ван_Россум,_Гвидо).

**Python** - это высокоуровневый язык программирования, который широко применяется в веб-разработке, сценариях, научных вычислениях, программах искусственного интеллекта и других областях.

Язык очень популярен и используется такими организациями, как Google, NASA, CIA и Disney.



## Немного о программировании

**Программирование** является процессом написания компьютерных (и не только) программ. В настоящее время программы окружают нас повсюду: от холодильника до запуска ракет в космические путешествия. В обыденной жизни программирование - это взаимосвязь творчества и точных данных и умение с этими данными работать. Писать книгу или писать код - нет абсолютно никакой разницы, поэтому **программист** - **это** прежде всего **творец**. Именно программист создает нечто "живое" из ничего. 

Вот мы и побудем немного творцами, вернее научимся ими быть

## Почему Python?

![img](https://habrastorage.org/r/w1560/webt/1d/ph/xg/1dphxgnkmgf0m-tbq8uxnqxuqzy.jpeg)

Вот рейтинг языков программирования согласно индексу TIOBE. Как можно заметить - Python занимает вторую позицию, и его популярность только растет с каждым годом.

Популярность Python также подстёгивает значительный рост сферы **Data Science**, где Python считается приоритетным языком.

Помимо **Data Science** Python используется в медицине, веб-разработке, написании чат-ботов, создании скриптовых программ и много-много где ещё (всё не перечислить)

Относительный лаконизм языка Python позволяет создать программу, которая будет гораздо короче своего аналога, написанного на статическом языке. Исследования показали, что программисты пишут примерно одинаковое количество строк кода каждый день независимо от языка, поэтому Python может значительно повысить вашу продуктивность. 

Язык программирования Python — самое несекретное оружие многих компаний, которым важна продуктивность работы сотрудников. Python является самым популярным языком на курсах программирования для начинающих в лучших американских колледжах (http://bit.ly/popular-py). Он также используется для оценки навыков программирования более чем 2000 работодателей (http://bit.ly/langs-2014).

## Начало работы

Вы можете скачать Python с официального сайта: https://www.python.org/
Также вы можете скачать бесплатную IDE от JetBrains: https://www.jetbrains.com/ru-ru/pycharm/download/

![img](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/217d5ea0-623d-40b1-9b31-027b904a5f15/dccudp7-221d1133-f3c3-48eb-a72c-c511828a1ff4.png)

*Примечание. Все примеры и весь код относится к Python версии 3.9*

 У языка существует множество различных реализаций, мы будем использовать **CPython**.

**CPython** — наиболее распространённая, де-факто  [эталонная реализация](https://ru.wikipedia.org/wiki/Эталонная_реализация_(информатика)) языка программирования Python. 
CPython является [интерпретатором](https://ru.wikipedia.org/wiki/Интерпретатор) [байт-кода](https://ru.wikipedia.org/wiki/Байт-код), написан на [C](https://ru.wikipedia.org/wiki/Си_(язык_программирования)). Разработка ведётся группой разработчиков под руководством создателя Python [Гвидо ван Россума](https://ru.wikipedia.org/wiki/Гвидо_ван_Россум). CPython является [программным обеспечением с открытым исходным кодом](https://ru.wikipedia.org/wiki/Открытое_программное_обеспечение).

Кроме CPython, существуют другие реализации Python: [Jython](https://ru.wikipedia.org/wiki/Jython), [IronPython](https://ru.wikipedia.org/wiki/IronPython), [PyPy](https://ru.wikipedia.org/wiki/PyPy) и [Stackless Python](https://ru.wikipedia.org/wiki/Stackless_Python).

## Дзен Python

Своё знакомство с языком мы начнем с вот такой программы

```python
import this
```

Она еще более известна, как "Дзен Python". Небольшая программа, которая рассказывает основные положения языка Python, его идеологию и основные принципы программирования.

После запуска этой программы мы увидим следующее:

``` python
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
```

Если перевести эти строки на русский язык, то получится что-то наподобие этого:

*Красивое лучше, чем уродливое.* 
*Явное лучше, чем неявное.* 
*Простое лучше, чем сложное.* 
*Сложное лучше, чем запутанное.*
*Одноуровневое лучше, чем вложенное.*
*Разреженное лучше, чем плотное.*
*Читаемость имеет значение.* 
*Особые случаи не настолько особые, чтобы нарушать правила.* 
*При этом практичность важнее безупречности.*
 *Ошибки никогда не должны замалчиваться.*
 *Если не замалчиваются явно.*
 *Встретив двусмысленность, отбрось искушение угадать.* 
*Должен существовать один — и желательно только один — очевидный способ сделать это.* 
*Хотя он поначалу может быть и не очевиден, если вы не голландец.* 
*Сейчас лучше, чем никогда.* 
*Хотя никогда зачастую лучше, чем прямо сейчас.* 
*Если реализацию сложно объяснить — идея плоха.* 
*Если реализацию легко объяснить — идея, возможно, хороша.*
*Пространства имен — отличная штука! Будем делать их побольше!*

## Первая программа

Давайте попробуем подумать, понять или угадать, что сделает следующая программа:

```python
fruit_prices = {
    'apple' : 100,
    'orange' : 150,
    'banana' : 125
}

fruit = 'apple'
price = fruit_prices[fruit]
print(f'You bought {fruit} at {price}$')
```

А если так:

``` python
цены_фруктов = {
    'яблоко' : 100,
    'апельсин' : 150,
    'банан' : 125
}

фрукт = 'яблоко'
цена = цены_фруктов[фрукт]
print(f'Вы купили {фрукт} за {цена}$')
```

Как можно заметить ничего страшного в Python нет. Практически все ключевые слова и команды имеют явную семантику. Просто представьте, что вы говорите программе:

1. Сделай действие 1
2. Сделай действие 2
3. И т. д. 

*Примечание. Несмотря на то, что Python поддерживает написание русских символов в названиях переменных, мы будем прибегать к их использованию в ОЧЕНЬ редких случаях*

Давайте теперь напишем стандартную программу:

``` python
print('Hello, world!')
```

Вот и всё. А теперь для сравнения та же самая программа на языке программирования C#

``` c#
using System;

class Program
{
 public static void Main(string[] args)
 {
 Console.WriteLine("Hello, world!");
 }
}
```

Ну, кажется, что в Python всё немного проще... И как бы да, и как бы нет - везде есть свои плюсы и минусы. Запомните, что главное знать - основы программирования, а не какой-то определённый язык. Язык Программирования обычно подбирается под какую-то определенную задачу.

## Типы данных - основы основ

Давайте подумаем как язык программирования работает вот с этими двумя объектами?

```python
42
'42'
```

Кажется, что эти объекты и выделяются по-разному. Почему-то одно число написано просто так, а второе в кавычках... Дело в том, что перед вами представлены совершенно разные объекты с точки зрения компьютера (вернее программы интерпретатора). Первый объект - это число, второй объект - это целое число.

От того какого типа данных объект - зависит какие у него свойства, возможные операции и т. д. Мы будем проходить типы данных последовательно: от более простых к более сложным. Для разных объектов одна и та же операция может быть определена по-разному.

Как это осознать? Ну, например. Давайте рассмотрим вектор с координатами (3, 4). Его длина составляет 5. А теперь подумайте, можем ли мы посчитать длину числа 7? Ну может быть и можем, просто взять модуль, но у вектора мы считал и длину всё равно по-другому. А почему? Да потому что - это разные объекты с точки зрения математики. 

Ниже представлены основные типы данных в Python. (Не переживайте мы научимся создавать собственные типы данных)

| Тип данных                   | Пример объекта           | Пример операций                      |
| ---------------------------- | ------------------------ | :----------------------------------- |
| int (целое число)            | 42                       | 42 + 42 = 84                         |
| float (число с плав. точкой) | 3.14                     | 10.3 + 16.7 = 27.0                   |
| complex (комплексное число)  | 1 + 2j                   | 1j*1j = (-1+0j)                      |
| bool (логический тип)        | True, False              | True + False = True                  |
| string (строка)              | 'foo', "bar", """text""" | '42' + "42" = "4242"                 |
| list (список)                | [1, True, 3.14, 'foo']   | [42, 100] + [True] = [42, 100, True] |
| dict (словарь)               | {'cat' : 42}             | Пока пропустим                       |
| type (специальный тип)       | type()                   | Тоже пропустим                       |
| function (функция)           | def f(): ...             | И тут тоже пропустим                 |

Чтобы определить какого типа объект, можно вызвать специальную "функцию" type() от объекта, например:

``` python
>>>type(42)
<class 'int'>
```

 Получили тип ```int```.

Создавая новый объект, мы можем сразу указать ему тип, а можем и не указывать. Python - динамически типизированный ЯП, в отличие от языков семейства С, в них необходимо ЯВНО указывать тип переменной, например так (Сравним Python и C#):

```python
number = 42
```

```c#
int number = 42
```

Хотя в Python, мы можем сделать так:

``` python
number: int = 42
```

Тут среда разработки (IDE) может сразу же понять какого типа переменная; таким образом, мы исключим множество ошибок.

Давайте более детально изучим числовые типы данных

## Переменные. Числовые типы данных.

Перед тем, как завести речь о числовых типах данных, давайте поймем, что такое **переменная**.

В Python всё — булевы значения, целые числа, числа с плавающей точкой, строки и даже крупные структуры данных, функции и программы — реализовано как объект. Это позволяет языку быть стабильным (и дает полезные особенности), чего не хватает некоторым другим языкам.

Объект похож на прозрачный пластиковый ящик, который содержит фрагмент данных. Объект имеет тип вроде булевых значений или целых чисел, который определяет, что можно сделать с этими данными. В реальном мире ящик с надписью «Керамика» может сообщить некоторую информацию (скорее всего, он тяжелый и лучше не ронять его на пол). Точно так же и в Python — если объект имеет тип int, вы знаете, что сможете сложить его с другим объектом типа int.

В следующем примере целое число 42 присваивается переменной num, а затем на экран выводится значение, связанное в текущий момент с этой переменной:

``` python
>>> num = 42
>>> print(num)
42
```

Сейчас пришло время сделать очень важное заявление о переменных в Python: переменные — это просто имена. Присваивание **не копирует** значение, оно прикрепляет **имя к объекту**, который содержит данные. Имя — это **ссылка** на какой-то объект, а не сам объект. Имя можно рассматривать как стикер.

Давайте рассмотрим как происходит присваивание ссылки, для этого рассмотрим следующий код:

``` python
>>> num1 = 42
>>> num2 = 42
>>> id(num1)
1963129408
>>> id(num2)
1963129408
```

Функция ```id(var: object)``` принимает на вход переменную типа Объект и возвращает некоторое число - адрес памяти, где данных объект хранится.

1. В первой строке выделяется память и создается объект ```42``` в памяти по адресу  ```1963129408``` (адрес выбирается "случайно")
2. Создается ссылка на объект по этому адресу из переменной ```num1```
3. Создается ссылка на объект по этому адресу из переменной ```num2```

Как мы можем заметить - объекты ссылаются на один и тот же объект в памяти.

*Примечание: объекты удаляются (следовательно и освобождают память) тогда, когда на них НЕ ССЫЛАЕТСЯ ни одно имя*

 **ВАЖНО:** в Python **ВСЁ - ЕСТЬ ОБЪЕКТ!**

### Числовой тип int. Операции.

Думаю, что тип int - самый любимый среди всех. Это же просто числа и всё.

Вот возможные операции над числами

| Название              | Обозначение | Пример                           | Результат | Тип возвращаемого значения |
| --------------------- | ----------- | -------------------------------- | --------- | -------------------------- |
| Сложение              | +           | 5 + 2                            | 7         | int                        |
| Вычитание             | -           | 5 - 2                            | 3         | int                        |
| Умножение             | *           | 5 * 2                            | 10        | int                        |
| Деление               | /           | 5 / 2<br />(вернет объект float) | 2.5       | float                      |
| Остаток от деления    | %           | 5 % 2                            | 1         | int                        |
| Целочисленное деление | //          | 5 // 2                           | 2         | int                        |
| Возведение в степень  | **          | 5 ** 2                           | 25        | int                        |
| Сравнение (Не равно)  | == (!=)     | 5 == 2                           | False     | bool                       |
| Больше (либо равно)   | > (>=)      | 5 > 2                            | True      | bool                       |
| Меньше (либо равно)   | < (<=)      | 5 < 2                            | False     | bool                       |

Так как Python очень широко используется в научных вычислениях, то в Python все операции делаются строго с математическими правилами, значит о скобках можно забыть.

Более того, в Python реализована длинная арифметика для типа int. Это означает, что если вы работаете с большими числами, то не надо париться и думать "влезет ли это число в тип данных по памяти или нет?". Например, в C# тип ```int``` хранит числа от -65536 до 65535 (включая 0), для более больших чисел, надо использоваться спец. тип ```longint```. 

В Python мы можем сделать так:

``` python
>>> 200 ** 200
16069380442589902755419620923411626025222029937827928353013760000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Вот, пожалуйста!

### Тип float.

Операции те же самые. Только вот числа хранятся в памяти по-другому, подробнее про это, можно почитать [тут](https://ru.wikipedia.org/wiki/Число_с_плавающей_запятой):

### Тип complex.

Нужен для работы с комплексными числами. В разработке применяется крайне редко. Ну и сравнивать два комплексных числа на "больше или меньше" нельзя! Потому что нет линейного порядка.

## Строковый тип данных string.

Важно, во многих языках программирования используются два различных строковых типа данных ```char``` и ```string``` - первый используется для создания единичных символов, а ```string``` представляет из себя последовательность ```char```. В Python - хоть что это ```str```

Вот пример на Python и C#

```python
# Писать можно и в '' , и в "", и даже в """""", но об этом попозже :)
c = "a"
s = 'hello world!'
```

```c#
char c = 'a' // Только в одинарных
string s = "hello world!" // Только в двойных
```

Раз ```string``` - уже другой тип данных, то и операции с ним уже другие. У строк существуют так называемые **методы** - специальный функционал, который мы вызываем через точку:

```python
>>>s = "Hello world!"
>>>s.upper()
'HELLO WORLD!'
```

Вот таблица с методами для строк:

| Функция или метод                                      | Назначение                                                   |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| **S = 'str'; S = "str"; S = '''str'''; S = """str"""** | [Литералы строк](https://pythonworld.ru/tipy-dannyx-v-python/stroki-literaly-strok.html) |
| **S = "s\np\ta\nbbb"**                                 | Экранированные последовательности                            |
| **S = r"C:\temp\new"**                                 | Неформатированные строки (подавляют экранирование)           |
| **S = b"byte"**                                        | Строка [байтов](https://pythonworld.ru/tipy-dannyx-v-python/bajty-bytes-i-bytearray.html) |
| **S1 + S2**                                            | Конкатенация (сложение строк)                                |
| **S1 \* 3**                                            | Повторение строки                                            |
| **S[i]**                                               | Обращение по индексу                                         |
| **S[i:j:step]**                                        | Извлечение среза                                             |
| **len**(S)                                             | Длина строки                                                 |
| **S.find**(str, [start],[end])                         | Поиск подстроки в строке. Возвращает номер первого вхождения или -1 |
| **S.rfind**(str, [start],[end])                        | Поиск подстроки в строке. Возвращает номер последнего вхождения или -1 |
| **S.index**(str, [start],[end])                        | Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError |
| **S.rindex**(str, [start],[end])                       | Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError |
| **S.replace**(шаблон, замена[, maxcount])              | Замена шаблона на замену. maxcount ограничивает количество замен |
| **S.split**(символ)                                    | Разбиение строки по разделителю                              |
| **S.isdigit**()                                        | Состоит ли строка из цифр                                    |
| **S.isalpha**()                                        | Состоит ли строка из букв                                    |
| **S.isalnum**()                                        | Состоит ли строка из цифр или букв                           |
| **S.islower**()                                        | Состоит ли строка из символов в нижнем регистре              |
| **S.isupper**()                                        | Состоит ли строка из символов в верхнем регистре             |
| **S.isspace**()                                        | Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v')) |
| **S.istitle**()                                        | Начинаются ли слова в строке с заглавной буквы               |
| **S.upper**()                                          | Преобразование строки к верхнему регистру                    |
| **S.lower**()                                          | Преобразование строки к нижнему регистру                     |
| **S.startswith**(str)                                  | Начинается ли строка S с шаблона str                         |
| **S.endswith**(str)                                    | Заканчивается ли строка S шаблоном str                       |
| **S.join**(список)                                     | Сборка строки из списка с разделителем S                     |
| **ord**(символ)                                        | Символ в его код ASCII                                       |
| **chr**(число)                                         | Код ASCII в символ                                           |
| **S.capitalize**()                                     | Переводит первый символ строки в верхний регистр, а все остальные в нижний |
| **S.center**(width, [fill])                            | Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию) |
| **S.count**(str, [start],[end])                        | Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию) |
| **S.expandtabs**([tabsize])                            | Возвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелам |
| **S.lstrip**([chars])                                  | Удаление пробельных символов в начале строки                 |
| **S.rstrip**([chars])                                  | Удаление пробельных символов в конце строки                  |
| **S.strip**([chars])                                   | Удаление пробельных символов в начале и в конце строки       |
| **S.partition**(шаблон)                                | Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки |
| **S.rpartition**(sep)                                  | Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий две пустых строки, а затем саму строку |
| **S.swapcase**()                                       | Переводит символы нижнего регистра в верхний, а верхнего – в нижний |
| **S.title**()                                          | Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний |
| **S.zfill**(width)                                     | Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями |
| **S.ljust**(width, fillchar=" ")                       | Делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar |
| **S.rjust**(width, fillchar=" ")                       | Делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar |
| **S.format**(*args, **kwargs)                          | [Форматирование строки](https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html) |

Подробнее о строках мы поговорим чуть позже!

## Превращение str в int и наоборот.

Мы всегда можем превратить любое число в строку, делается это так:

```python
>>>num = 1000
>>>num = str(num)
>>>type(num)
<class 'str'>
```

А вот обратно, вообще говоря, не всегда:

```python
>>> s = '42'
>>> s = int(42)
>>> type(s)
<class 'int'>
>>> s = 'hello'
>>> s = int(s)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s = int(s)
ValueError: invalid literal for int() with base 10: 'hello'
```

Как можно заметить, если мы не можем превратить строку в число, то выпадает ошибка ```ValueError```.

Более того, мы можем превращать одни числовые типы в другие без опасения, если мы превращаем более частный тип в более общий(**upcasting**), если мы превращаем наоборот, то могут возникнуть некоторые проблемы (**downcasting**). Например: мы ведь можем сказать, что любое натуральное число является целым, но обратно мы так сказать можем не всегда. То есть число 5 - это натуральное число (следовательно целое, т. к. натуральные более частный тип), но не всякое целое - это натуральное, к примеру число 0.

Пример:

```python
# При переводе из числа с плав. точкой в целое число мы теряем в точности
>>> num = 5.3
>>> num = int(num)
>>> num
5
```

``` python
# А вот обратно уже нет
>>> num = 42
>>> num = float(42)
>>> num
42.0
```