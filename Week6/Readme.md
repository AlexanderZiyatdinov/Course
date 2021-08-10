# Globals. Locals. Scopes. Closure. Namespaces.

# Замыкания. Closures.

![img](https://habrastorage.org/r/w1560/webt/jq/8t/d7/jq8td7tlv71kv-iby97mqqt9iyk.jpeg)

**Важно:** Некоторые примеры будут разобраны в **интерактивном** режиме Python.

Мы можем определить функцию внутри другой функции, ну, например, так:

```python
>>> def outer(a, b):
		def inner(c, d):
	    	return c + d
		return inner(a, b)

>>> outer(4, 7)
11
```

Внутренние функции могут быть полезны при выполнении некоторых сложных задач более одного раза внутри другой функции. Это позволит избежать использования циклов или дублирования кода. Рассмотрим пример, когда внутренняя функция добавляет что-то своё к исполнению внешней:

```python
>>> def foo(a, b):
		print(a)
		def bar(c, d=5):
			print(c)
			return c * d
		return bar(b)

>>> foo(5, 3)
5
3
15
```

Как можно заметить, внутренняя функция - такой же полноправный объект, как и внешняя.

**Замыкания**. Внутренняя функция может действовать как **замыкание**. **Замыкание** — это функция, которая динамически генерируется другой функцией. Обе они могут изменяться и запоминать значения переменных, которые были созданы вне функции

Вернемся к нашему примеру, только немного перепишем его:

```python
>>> def foo(a, b):
		def bar(d=5):
			return b * d
		return bar
```

Функция `bar` знает значение переменной `b`, которое было передано в функцию `foo`, и запоминает это значение.  `foo` возвращает некоторый объект `function` (копию функции `bar`), но не вызывает его. Получается своего рода **замыкание**: динамически созданная функция, которая запоминает, откуда она появилась, следовательно она не уничтожается сборщиком мусора, ведь на неё есть ссылка.

Вызовем функцию `foo` несколько раз

```python
>>> a = foo(5, 3)
>>> b = foo(6, 4)

>>> type(a)
<class 'function'>
>>> type(b)
<class 'function'>

>>> a
<function foo.<locals>.bar at 0x000002104FF85550>
>>> b
<function foo.<locals>.bar at 0x000002104FF855E0>
```

Как мы видим они являются и функциями и замыканиями одновременно.

Теперь, если мы их вызовем, то по идее, раз это **замыкания**, то они должны помнить, что за аргументы им передавались.

```python
>>> a()
15
>>> b()
20
```

Далее поговорим про области видимости:

## Пространства имен и области видимости. Namespaces & Scopes.

**Пространство имен** — это совокупность определенных в настоящий момент символических имен и информации об объектах, на которые они ссылаются. Вы можете рассматривать такое пространство как словарь, в котором ключи являются именами объектов, а значения — самими объектами. Каждая пара ключ-значение соотносит имя с соответствующим ему объектом.

> *Пространства имен — отличная штука! Будем использовать их чаще! — Тим Петерс в “Дзен Python”.*

Существует 4 типа пространств имен:

1. Встроенное.
2. Глобальное.
3. Объемлющее.
4. Локальное.

### Встроенное (B - builtins)

**Встроенное** пространство имен представляет из себя коллекцию объектов, которые всегда доступны во время работы Python.

```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

Встроенное пространство имен создается при запуске программы интерпретатором и уничтожается после завершения работы программы

### Глобальное (G - global)

**Глобальное пространство имен** содержит переменные, которые определены на уровне Python программы, оно создается при запуске программы и уничтожается после завершения работы интерпретатора. 

Более того, глобальная область видимости может создаваться и для любого пакета, который мы импортируем в наш проект с помощью `import`.

### Объемлющее (E - enclosed)

**Объемлющим пространством имен** можно назвать такое пространство имен **E**, что всем включенным в него другим пространством имен будут доступны все имена из **E**.

### Локальное пространство имен (L - local)

**Локальное пространство имен** содержит имена, определенные в некотором отдельном блоке кода, например в функции.

## Области видимости

Теперь рассмотрим пример, в котором указаны все пространства имен.

```python
a = 10
def foo():
    print('foo')
    
    def bar():
        print('bar')
        return 
    bar()
    return
```

* **Встроенное пространство имен** содержится по умолчанию в программе, как мы это выяснили ранее
* **Глобальное пространство имен** содержит объекты `a` и `foo`
* **Объемлющее пространство имен** содержится во всех строках, кроме первой
* **Локальное пространство имен** содержится внутри функции `bar`

Можно сказать, что функция `foo` является объемлющим пространством имен для функции `bar`, но также можно сказать, что вся программа является объемлющим пространством имен для функции `foo`.

**Область** **видимости** - место где определяются переменные и выполняется их поиск. Всегда, когда в программе используется какое то имя, интерпретатор создает, изменяет или отыскивает это имя в пространстве имен – в **области**, где находятся имена.

То есть у нас программе может быть несколько одинаковых переменных, которые будут ссылаться на разные объекты.

```python
x = 100
def foo():
    for x in range(3):
        print(x)

foo()
print(x)

# Выведет:
0
1
2
100
```

Как мы видим переменная `x=100` объявлена в глобальном пространстве имен, а переменная `x`, участвующая в цикле, объявлена в локальном пространстве имен, соответственно они находятся в разных областях видимости, то есть программа воспринимает их как два соверешенно не связанных имени.

Предположим, что у нас есть несколько имен `x` в программе, тогда же как будет осуществляться поиск нужной `x `? А вот так вот:

Python будет искать его следующих областях видимости в таком порядке:

1. **Локальная.** Если вы ссылаетесь на `x` внутри функции, то интерпретатор сначала ищет его в самой внутренней области, локальной для этой функции.
2. **Объемлющая.** Если `x` не находится в локальной области, но появляется в функции, располагающейся внутри другой функции, то интерпретатор ищет его в области видимости объемлющей функции.
3. **Глобальная.** Если ни один из вышеуказанных вариантов не принес результатов, то интерпретатор продолжит поиск в глобальной области видимости.
4. **Встроенная.** Если интерпретатор не может найти `x` где-либо еще, то он направляет поиски во встроенную область видимости.

Эта последовательность составляет суть **правила областей видимости LEGB,** как его обычно называют в публикациях о Python (хотя, на самом деле, данный термин не встречается в его официальной документации). Интерпретатор начинает поиски имени изнутри, последовательно переходя от локальной области видимости к объемлющей, затем к глобальной и в завершении к встроенной.

![img](https://miro.medium.com/max/549/0*QNAUDYhabPbUhFzk.png)



## Locals & Globals

Чтобы узнать какие пременные содержатся в глобальном пространстве имен, достаточно написать `globals()`:

```python
a = 10

def foo():
    pass

print(globals())

# Выведет:
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002A604946D00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'Путь_до_файла', '__cached__': None, 'a': 10, 'foo': <function foo at 0x000002A604CDF040>}
```

Чтобы узнать какие переменные содержатся в локальном пространстве имен, надо написать `locals()`:

```python
a = 10

def foo():
    a = 9
    b = 8
    print(locals())
foo()

# Выведет:
{'a': 9, 'b': 8}
```

### Прокидываем значение из глобального пространства имен внутрь функции

Иногда хочется поменять значение глобальной переменной внутри функции, вот так:

```python
a = 10
def foo():
    a = 42
   
foo()
print(a)

# Выведет:
10
```

Но, как мы видим это не работает. Чтобы свершился необходимый нам сценарий, надо написать оператор `global` перед инициализацией переменной внутри функции:

```python
a = 10
def foo():
    global a
    a = 42
   
foo()
print(a)

# Выведет:
42
```

### Прокидываем значение из объемлющего пространства имен внутрь локального

Чтобы поменять значение переменной из внешней функции во внутренней, необходимо написать оператор `nonlocal` перед инициализацией переменной внутри вложенной функции:

``` python
def foo():
    a = 10
    def bar():
        nonlocal a
        a = 42
    bar()
    print(a)

foo()

# Выведет:
42
```
