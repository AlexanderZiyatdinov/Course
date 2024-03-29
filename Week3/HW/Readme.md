# Домашнее задание 3

## Вопросы для самопроверки:

1. Может ли `list` быть ключом в словаре?
2. Как превратить `list` в `set`?
3. Каким будет результат функции `bool([[]])`?
4. Какой тип у объекта `print()`?
5. Какой тип у объекта `print`?

## Задачи

### Управление роботом

![img](https://cs5.pikabu.ru/post_img/big/2014/11/13/10/1415900346_862823306.jpg)

#### Условие:

Скачайте [проект](https://github.com/AlexanderZiyatdinov/Course/raw/main/Week3/HW/5.%20Robot.zip)

В файле ```robot``` допишите программу - одну единственную строку.

В воскресенье Вася пошел в кружок робототехники и увидел там такой код управления боевым роботом:

```python
def should_fire(enemyInFront: bool, enemyName: str, robotHealth: int) -> bool:
    shouldFire: bool = True
    if enemyInFront:
        if enemyName == "boss":
            if robotHealth < 50:
                shouldFire = False
            if robotHealth > 100:
                shouldFire = True
    else:
        return False
    return shouldFire
```

Код показался Васе слишком длинным, а к тому же еще и неряшливым. Вася поспорил с автором, что сможет написать функцию, делающую ровно то же самое, но всего в одну строку.

Кажется, Вася погорячился... Или нет? Помогите ему не проиграть в споре!

```python
def should_fire(enemyInFront: bool, enemyName: str, robotHealth: int) -> bool:
    return ... # ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
```

Проверьте своё решение, запустив тесты.

### Ближайший элемент

![img](http://risovach.ru/upload/2016/12/mem/morfeus_133517237_orig_.jpg)

#### Условие:

Это первое задание, для которого потребуется сторонняя библиотека, которой нет в начальной сборке Python.

Для установки библиотеки `NumPy` нам потребуется написать следующее в консоли:

**``` pip install numpy```**

После этого, мы сможем писать в наших программах следующее:

```python
import numpy as np # Всегда пишут так!
# Теперь мы можем взаимодействовать с библиотекой numpy через имя np
```

Скачайте [проект](https://github.com/AlexanderZiyatdinov/Course/raw/main/Week3/HW/6.%20Nearest_Value.zip)

Реализуйте функцию, принимающую на вход квадратную матрицу `X` и некоторое число `a` и возвращающую ближайший к числу элемент матрицы. 
Если ближайших несколько - выведите минимальный из ближайших. (Вернуть нужно само число, а не индекс числа!)

В файле ```nearest_value``` напишите функцию, которая вернет ближайший элемент в соответствии с вышеописанным условием.

Про матрицы можете почитать [тут](https://thecode.media/matrix-101/). Вам может пригодится прибавление (вычитание) к матрице числа, поиск максимального (минимального) элемента и поиск индекса. Всё это уже реализовано в файле `numpy`.

Вот примеры использований функций и операций:

```python
# Создание квадратной матрицы
import numpy as np

X = np.array([[ 1,  2, 13],
              [15,  6,  8],
              [ 7, 18,  9]])
```

``` python
# Сложение с числом
print(X + 5)

# Выведет:
array([[ 6,  7, 18],
       [20, 11, 13],
       [12, 23, 14]])
```

```python
# Навешивание модуля
X = np.array([[ 1,  2, 13],
              [-15,  6,  8],
              [ 7, -18,  9]])

print(abs(X))
# Выведет:
[[ 1  2 13]
 [15  6  8]
 [ 7 18  9]]
```

``` python
# Поиск максимального элемента
X = np.array([[ 1,  2, 13],
              [-15,  6,  8],
              [ 7, -18,  9]])

print(X.max())

# Выведет:
13
```

```python
# Поиск индекса элемента

X = np.array([[ 1,  2, 13],
              [-15,  6,  8],
              [ 7, -18,  9]])

print(np.where(X == 13))
# Выведет:
(array([0], dtype=int64), array([2], dtype=int64))
```

По всем вопросам сначала [сюда](https://pyprog.pro/reference_manual.html)

### ![Эмодзи 🇷🇺 ВКонтакте](https://vk.com/emoji/e/f09f87b7f09f87ba_2x.png) Рубль против Доллара ![Эмодзи 🇺🇸 ВКонтакте](https://vk.com/emoji/e/f09f87baf09f87b8_2x.png)

Скачайте [проект](https://github.com/AlexanderZiyatdinov/Course/raw/main/Week3/HW/7.%20Dollars.zip)

Необходимо написать программу, которая может принимать несколько аргументов, в зависимости от которых выводит то или иное значение. Пользователь в первой строке вводит одну из двух букв `r` или `d`. Во второй строке пользователь вводит целое число от 1 до 100. 

После ввода значений пользователя программа должна вывести сообщение вида ```100 рублей``` или ```31 доллар```

**Примеры:**

```python
#Ввод:
d
31
#Вывод:
31 доллар
```

```python
#Ввод:
r
23
#Вывод:
23 рубля
```

Обратите внимание, что слово при выводе **может склоняться** по правилам русского языка.

Напишите весь функционал внутри функции ```main```.

Проверьте свое решение запустив тесты.
