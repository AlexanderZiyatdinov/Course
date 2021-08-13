# Домашнее задание 8

На этой неделе немного займемся алгоритмикой, поэтому некоторые задачи будем решать на платформе timus. Там как раз есть банк открытых олимпиадных задач.



Вы можете там зарегистрироваться и сдавать решения проверяющей системе, либо можете кидать решение текстом мне.

# Задание 1

[Условие](https://acm.timus.ru/problem.aspx?space=1&num=1086)

# Задание 2

[Условие](https://acm.timus.ru/problem.aspx?space=1&num=1025)

# Задание 3

Вам дана некоторые функции:

```python
def my_sort_algorithm_one(array: list[int]) -> list[int]:
    pass


def my_sort_algorithm_two(array: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    from random import randint as rnd

    array = [rnd(1, 1000) for _ in range(10000)]

    result_1 = my_sort_algorithm_one(array=array.copy())
    result_2 = my_sort_algorithm_two(array=array.copy())
    assert result_1 == result_2, 'Lists are not equal'
    print('Lists are equal')
```

Необходимо написать два любых алгоритма сортировки целочисленного массива. 

Проверкой того, что вы всё сделали правильно, послужит надпись `'Lists are equal'` после выполнения программы.

Дополнительно:

Сделай обработку ошибки, если функция вместо списка получит какой-то другой тип данных, например словарь.

