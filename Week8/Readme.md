# Исключения. Обработка ошибок.

> Это видео, если что 😄

[![Video](https://i.ytimg.com/vi/j3sks_CJoZ0/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAs9nWr8QLVVePbrvhgOpfQL6vwvA)](https://www.youtube.com/watch?v=j3sks_CJoZ0)

[![Video](https://i.ytimg.com/vi/svT2CETQIws/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAxOc8MhKRrawcSbN-sbXG3P-R2LQ)](https://www.youtube.com/watch?v=svT2CETQIws)

## Исключения

Обычно, при работе программы, запрашиваются дополнительные ресурсы у операционной системы. Нередко во время выполнения кода ОС не отвечает взаимностью, например:

* Мы запрашиваем память, а памяти больше нет
* Мы устанавливаем соединение с каким-нибудь удалённым узлом, но соединение было разорвано
* Взаимодействовали с внешним устройством, но не получили доступ к нему
* Пытались создать объект `5 / 0`, но не смогли этого сделать

На такие случаи Python выдаст **исключение** - т. е. скажет, что вы нарушили некоторые правила языка Python, вследствие чего программа не выполнится.

### Типичные ошибки

Мы уже не раз сталкивались с какими-то исключениями в во время работы наших программ: деление на ноль, обращение к несуществующему индексу коллекции (Iterable object), вызов несуществующего метода у объекта, неверный вызов функции и т. д. и т. п.

Давайте посмотрим на примеры таких программ:

```python
a = 5
a / 0

---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-80260b7fb74c> in <module>
      1 a = 5
----> 2 a / 0

ZeroDivisionError: division by zero
```

Посмотрим на вывод "под микроскопом" и заметим, что Python:

* Вывел так называемый стек вызовов ошибок (про это поговорим чуть позже) `<ipython-input-1-80260b7fb74c> in <module>`
* Указал разновидность исключения `ZeroDivisionError`
* Указал строку, где было вызвано исключение `----> 2 a / 0`
* Написал пояснение исключения `division by zero`

Чтобы пользователь знал о происходящем, рекомендуется добавлять обработчики исключений везде, где исключение может быть сгенерировано. Не всегда у вас получится исправить ошибку, но вы хотя бы будете знать, при каких обстоятельствах она появилась, и аккуратно завершите программу. Если исключение сгенерировалось в функции и там не обработалось, оно будет всплывать до тех пор, пока его не поймает соответствующий обработчик в одной из вызывающих функций. Если вы не предоставите собственный обработчик исключений, Python выведет сообщение об ошибке и некоторую информацию о том, где произошла ошибка, а затем завершит программу.

### Вложенные ошибки

Иногда, ошибки могут быть допущены внутри вложенных конструкций. Для наглядной иллюстрации рассмотрим пример в интерактивном режиме:

```python
>>> def f():
    print('f')
    def g():
        a = [1, 2, 3]
        return a[1000]
    return g
>>> func = f()
'f'
>>> func()
IndexError                                Traceback (most recent call last)
<ipython-input-4-bd1982955a12> in <module>
----> 1 func()

<ipython-input-2-0d322cd3883d> in g()
      3     def g():
      4         a = [1, 2, 3]
----> 5         return a[1000]
      6     return g

IndexError: list index out of range
```

Мы видим, что Python сначала вывел информацию о том, что ошибка была допущена во время вызова `func()`, а затем внутри этого вызова ошибка была допущена во время выполнения инструкции `return a[1000]` -- данная конструкция вывода ошибок и называется **стеком вызова**.

Python как бы постепенно раскрывает вызовы внутри кода, вплоть до строки с самой ошибкой.

### Отложенная ошибка

Иногда ошибки могут возникать откуда ни возьмись. Ну, например, разберем следующий сценарий работы:

> Необходимо написать функцию, которая бы принимала два аргумента, складывала бы их и возвращала результат. После чего, мы могли бы работать с полученным значением.

```python
def my_add(a, b):
    """Функция, которая складывает два числа и возвращает результат"""
    return a + b

result = my_add(5, 3)
new_result = result + 5
print(new_result)

# Выведет:
13
```

Отлично, всё работает или нет...

```python
def my_add(a, b):
    """Функция, которая складывает два числа и возвращает результат"""
    return a + b

result = my_add([5], [3])
new_result = result + 5
print(new_result)

# Выведет:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-11ec7ea760a2> in <module>
      4 
      5 result = my_add([5], [3])
----> 6 new_result = result + 5
      7 print(new_result)

TypeError: can only concatenate list (not "int") to list
```

Как мы можем заметить ошибка была допущена в строке `6`, однако настоящая ошибка была допущена в строке `return a + b`. Подразумевалось, что мы вернем какое-то число, а мы вернули список, следовательно в строке `6` и произошла ошибка. 

То есть ***Отложенная ошибка*** - это ошибка, которая происходит не в том месте, где она реально была допущена

Для обработки всех вышеизложенных ситуаций существуют специальные средства и инструменты в Python, теперь поговорим о них более детально:

## Обработка исключений

Для того, чтобы обработать какое-либо исключение вручную, необходимо написать конструкцию:

```python
try:
    блок_кода
except expression [as e]:
    блок_кода
else:
    блок_кода
finally:
    блок_кода
```

Python пытается выполнить код, который находится в `try`, и если исключений не возникает, то исполнение кода переходит в блок `else` и в конце выполняет еще блок `finally`.

Если же исключение возникло внутри `try`, то Python проверяет внутри блока `except` является ли исключение наследником `expression`, если это так, то в `e` записывается случившееся исключение и выполняет блок кода в этом `except` , и только в этом `except`.  И так далее проверятся все `except` и в конце выполнится `finally`.

## Генерация исключений

Для генерации собственных исключений используют конструкцию:

```python
raise [expression ["from" expression]]
```

Например, рассмотрим такой код:

```python
>>> raise ValueError
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise ValueError
ValueError
```

## Иерархия исключений

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

### Обзор исключений

- **BaseException** - базовое исключение, от которого берут начало все остальные.
  - **SystemExit** - исключение, порождаемое функцией sys.exit при выходе из программы.
  - **KeyboardInterrupt** - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
  - **GeneratorExit** - порождается при вызове метода close объекта generator.
  - **Exception** - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
    - **StopIteration** - порождается встроенной функцией next, если в итераторе больше нет элементов.
    - ArithmeticError - арифметическая ошибка.
      - **FloatingPointError** - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
      - **OverflowError** - возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
      - **ZeroDivisionError** - деление на ноль.
    - **AssertionError** - выражение в функции assert ложно.
    - **AttributeError** - объект не имеет данного атрибута (значения или метода).
    - **BufferError** - операция, связанная с буфером, не может быть выполнена.
    - **EOFError** - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
    - **ImportError** - не удалось импортирование модуля или его атрибута.
    - **LookupError** - некорректный индекс или ключ.
      - **IndexError** - индекс не входит в диапазон элементов.
      - **KeyError** - несуществующий ключ (в словаре, множестве или другом объекте).
    - **MemoryError** - недостаточно памяти.
    - **NameError** - не найдено переменной с таким именем.
      - **UnboundLocalError** - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
    - **OSError** - ошибка, связанная с системой.
      - **BlockingIOError**
      - **ChildProcessError** - неудача при операции с дочерним процессом.
      - **ConnectionError** - базовый класс для исключений, связанных с подключениями.
        - **BrokenPipeError**
        - **ConnectionAbortedError**
        - **ConnectionRefusedError**
        - **ConnectionResetError**
      - **FileExistsError** - попытка создания файла или директории, которая уже существует.
      - **FileNotFoundError** - файл или директория не существует.
      - **InterruptedError** - системный вызов прерван входящим сигналом.
      - **IsADirectoryError** - ожидался файл, но это директория.
      - **NotADirectoryError** - ожидалась директория, но это файл.
      - **PermissionError** - не хватает прав доступа.
      - **ProcessLookupError** - указанного процесса не существует.
      - **TimeoutError** - закончилось время ожидания.
    - **ReferenceError** - попытка доступа к атрибуту со слабой ссылкой.
    - **RuntimeError** - возникает, когда исключение не попадает ни под одну из других категорий.
    - **NotImplementedError** - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
    - **SyntaxError** - синтаксическая ошибка.
      - **IndentationError** - неправильные отступы.
        - **TabError** - смешивание в отступах табуляции и пробелов.
    - **SystemError** - внутренняя ошибка.
    - **TypeError** - операция применена к объекту несоответствующего типа.
    - **ValueError** - функция получает аргумент правильного типа, но некорректного значения.
    - **UnicodeError**- ошибка, связанная с кодированием / раскодированием unicode в строках.
      - **UnicodeEncodeError** - исключение, связанное с кодированием unicode.
      - **UnicodeDecodeError** - исключение, связанное с декодированием unicode.
      - **UnicodeTranslateError** - исключение, связанное с переводом unicode.
    - **Warning** - предупреждение.

## Практика

Теперь хорошим упражнением будет: переписать код функции `my_add` так, чтобы обрабатывались всевозможные исключения, кстати функция `isinstance(value, type)` позволяет проверить является ли объект `value` типом `type`.
