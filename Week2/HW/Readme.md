# Домашнее задание 2

## Вопросы для самопроверки:

1. Как изменить строку ```str```?
2. Как превратить значение ```True``` в список ```['T', 'r', 'u', 'e']```?
3. Чем отличается ```tuple``` от ```list```?
4. Можем ли мы создать список внутри которого будет другой список? А список внутри которого будет кортеж?
5. Попробуйте создать кортеж внутри которого будет список, а затем измените этот список внутри кортежа... Можно ли так сделать или нет?

## Задачи

### Герои меча и магии

![img](https://i.ytimg.com/vi/8FNA4lNBvNo/maxresdefault.jpg)

![img](https://c10.patreonusercontent.com/3/eyJ3Ijo0MDB9/patreon-media/p/reward/5784374/eb875af965c64e00be10e78dbf8440fe/6.gif?token-time=2145916800&token-hash=KUAO0eD2qgoiMQQOcsEM2LMPqJBYDQAZpwGRGpdiriI%3D)

#### Условие:

Скачайте [проект](https://github.com/AlexanderZiyatdinov/Course/raw/main/Week2/HW/4.%20HoMM3.zip)

Есть такая игра - **[Герои меча и магии III](https://ru.wikipedia.org/wiki/Heroes_of_Might_and_Magic_III)** - некоторая пошаговая стратегия в стиле фэнтези. Одна из самых популярных игр в истории человечества. Кстати недавно вышла её HD [версия](https:/www.youtube.com/watch?v=2Mr6HJrDLjk). Ладно, что-то мы отвлеклись от темы, а то эту игру можно хвалить **бесконечно**.

![img](https://thumbs.gfycat.com/ExcellentGoodnaturedDiscus-max-1mb.gif)

Вам необходимо помочь существам Эрафии вернуться в свои жилища. Каждое существо принадлежит какой-то определенной локации.

Вот все локации:

* Замок (Castle)
* Оплот (Rampart)
* Башня (Tower)
* Инферно (Inferno)
* Некрополис (Necropolis)
* Подземелье (Dungeon)
* Цитадель (Stronghold)
* Крепость (Fortress)
* Сопряжение (Conflux)

В каждой из них живет по 7 существ (т. е. всего 7*9 = 63 существа), например: **Крестоносец** живет в **Замке**, а **Вампир-лорд** в  **Некрополисе**. 

Всё было хорошо и ничего не предвещало беды, но внезапно *[со звоном скрестились Ледяной клинок и клинок Армагеддона](https://www.youtube.com/watch?v=h4wfuqb-Rc0)*. Существа оказались перепутаны, кто-то остался в своем жилище, а кто-то попал в другое, помимо этого существа перепутали свои уровни: кто-то был первого уровня, а стал, например, седьмого. Ваша задача: вернуть всех существ на  своё место (т. е. в свой город и на свой уровень).

В файле ```towns``` описаны города с ошибочными существами.

Вот, пример использования:

```python
# Это просто пример!

import towns
castle = towns.castle
print(castle) ## Выведется:['Местер Гремлин', 'Стрелок', 'Королевский грифон', 'Крестоносец', 'Фанатик', 'Чемпион', 'Архангел'] 
castle[0] = "Алебардщик"
print(castle) ## Выведется:['Алебардщик', 'Стрелок', 'Королевский грифон', 'Крестоносец', 'Фанатик', 'Чемпион', 'Архангел']
# Всё ок, переменная castle "исправлена"
```

В файле ```HoMM3``` вы должны "**исправить**" переменные ```castle```, ```rampart```, ```tower```, ```inferno```, ```necropolis```, ```dungeon```, ```fortress``` и ```conflux```

Проверьте правильность выполнения задачи, запустив тесты в файле ```test```.

![img](https://static.goodgame.ru/files/avatars/av_45003_Eibk.gif)

Чтобы узнать где живут какие существа, достаточно открыть вот эту [статью](https://homm3sod.ru/units/). Все названия берутся В ТОЧНОСТИ с этой статьи. 

**Примечание:** В замках живут только **улучшенные** существа, чтобы вам было проще делать задачу, вам нужно смотреть только на **улучшенные версии существ в статье** (т. е. на каждое второе существо):

![image-20210719191901314](https://github.com/AlexanderZiyatdinov/Course/blob/main/Week2/HW/пример.gif)



