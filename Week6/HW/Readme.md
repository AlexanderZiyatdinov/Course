# Домашнее задание 6

## Вопросы для самопроверки:

1. Какие бывают аргументы у функции?
2. Что такое замыкание?
3. Что такое область видимости?
4. Сколько может быть глобальных пространств имен в одной программе?
5. Зачем нужны lambda функции?
6. Что такое globals, locals, global и nonlocal?

## PyTesseract OCR

![img](https://tudoprogramado.blog.br/assets/tesseract-ocr-e-python.jpg)

> Ну вот мы с вами уже и до Optical Character Recognition дожили...

**Условие:**

[Скачайте проект](https://github.com/AlexanderZiyatdinov/Course/raw/main/Week6/HW/OCR.zip)

Васе необходимо отправить огромную кучу различных документов по работе. Все документы имеют формат .pdf. Данные были сохранены так, что они не выделяются, то есть являются статичной картинкой. Такое часто бывает, правда же?

Вроде бы Вася уже всё закончил и даже ушел в отпуск, но внезапно обнаружил, что на всех документах содержится некая очепятка. К огромному сожалению, Вася уже загорает в другой стране (страна переводится с английского на русский, как слово "Индейка"), а все исходники остались у него дома. 

Помогите Васе исправить все документы, для этого напишите программу, которая бы умела распознавать текст на изображении.

> А, да. Вася еще сказал вам, что 90% времени его работы программистом уходит на то, что он гуглит как решается та или иная задача. 
> Он предлагает вам либо прочитать [документацию](https://tesseract-ocr.github.io/tessdoc/Home.html), либо обратиться к этому [сайту](https://stackoverflow.com/questions/37745519/use-pytesseract-ocr-to-recognize-text-from-an-image) (учтите он англоязычный)

В файле `help.py` допишите одну единственную функцию, которая будет реализовывать поставленную задачу.

Проверьте своё решение, запустив тесты.

В качестве тестового образца, используйте файл `img1.png`.

**Примечание:**

Для работы вам понадобится библиотека `pytesseract` и `open-cv`

То есть необходимо прописать в терминале:

```cmd
pip install tesseract
pip install opencv-python
```

**ВАЖНО:** Если у вас ОС семейства Windows, то сначала необходимо установить pytesseract с [сайта](https://tesseract-ocr.github.io/tessdoc/Downloads.html). 
Запомните расположение файла `tesseract.exe` Это вам еще понадобится.





