# Домашняя работа 9

## Вопросы для самопроверки

1. Что такое класс и зачем он нужен?
2. Что такое инкапсуляция?
3. Что такое ООП?
4. Какие модификаторы доступа вы знаете?
5. Что такое геттер и сеттер?

## Вектор

### Задача 1:

Создайте класс `Vector`, который описывает вектор (в трёхмерном пространстве).

У него должны быть:

* конструктор с параметрами в виде списка координат (могут быть нецелыми) `x, y, z`
* метод, вычисляющий длину вектора: ![$\sqrt{x^2 + y^2 + z^2}$](https://habrastorage.org/getpro/habr/formulas/25d/34a/0a1/25d34a0a162c05fc374870c02cd35c00.svg)
* метод, вычисляющий скалярное произведение: ![$x_1x_2 + y_1y_2 + z_1z_2$](https://habrastorage.org/getpro/habr/formulas/727/e36/48d/727e3648d68ee74f9a957180ce6345b0.svg)
* метод, вычисляющий векторное произведение с другим вектором: ![$(y_1z_2 - z_1y_2, z_1x_2 - x_1z_2, x_1y_2 - y_1x_2)$](https://habrastorage.org/getpro/habr/formulas/d7e/618/850/d7e61885091f40ffa8c70ab03566beb5.svg)
* метод, вычисляющий угол между векторами (или косинус угла): косинус угла между векторами равен скалярному произведению векторов, деленному на произведение модулей (длин) векторов: ![$\frac{(a,b)}{|a| \cdot |b|}$](https://habrastorage.org/getpro/habr/formulas/d0c/cd2/510/d0ccd2510a1d994d0d301ca0cedb4d6c.svg)
* методы для суммы и разности: ![$(x_1 + x_2, y_1 + y_2, z_1 + z_2)$](https://habrastorage.org/getpro/habr/formulas/ef0/c0e/628/ef0c0e628c68e5d995fdd30a1abba95d.svg) и ![$(x_1 - x_2, y_1 - y_2, z_1 - z_2)$](https://habrastorage.org/getpro/habr/formulas/909/7d8/961/9097d8961d27b3243cc575c074cf567f.svg). [Тык сюда, вам это 100% пригодится](http://habrahabr.ru/post/186608/#numeric)

Если метод возвращает вектор, то он должен возвращать новый объект, а не менять базовый.

### Задача 2:

Написать в отдельно файле `test_vector.py` тесты для каждого из методов класса `Vector`. 

Подробнее о модульном тестировании можно посмотреть [здесь](https://www.youtube.com/watch?v=lKo-F3gSl7I):
Либо в предыдущих проектах.

