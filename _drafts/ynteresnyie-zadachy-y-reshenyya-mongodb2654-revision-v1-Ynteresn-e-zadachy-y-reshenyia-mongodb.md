---
id: 2670
title: 'Интересные задачи и решения: mongodb'
date: 2018-02-04T15:09:32+02:00
author: alexrb
layout: revision
guid: http://alexrb.name/2018/02/2654-revision-v1/
permalink: /2018/02/2654-revision-v1/
---
Обратился ко мне один знакомый с &#8220;проблемой&#8221; &#8211; умер диск на dedicated, хостинг откатил бекап, но сайт лежит и информацию &#8220;вытащить&#8221; с него обычными способами получить не удается, а есть необходимость сохранить базу контактов пользователей. Задача относительно простая, за исключением одного но &#8211; есть только shell, а код никто не знает.<!--more-->

Закапываемся в код &#8211; php, что уже проще, структура папок подсказывает, что фреймворк использовали, который уже &#8220;умер&#8221;. Но тем не менее нахожу, что доступ к mysql, которого не было, не нужен (ура!) &#8211; инфо лежит в mongodb  (первый раз вижу этого &#8220;зверька&#8221;).  Как результат &#8211; &#8220;американские горки&#8221; настроения продолжаются.

Устанавливаю mongodb &#8211; пытаюсь просмотреть базу, там, где она лежит, но ничего не отображается (разбираюсь, что это &#8211; логично, ведь в настройках прописан путь, где искать базы). Копирую файлы в нужную папку, но все равно ничего не отображается. Еще какое-то время разбираюсь с тем, что мне нужно изменить права на файлы, чтобы пользователь mongodb имел и ним доступ. Бинго! Доступ получен, но информацию сложно назвать удобно читабельной, а тем более, копируемой. Следующий шаг &#8211; экспортировать из mongo во что-то более читабельное. Нахожу, что по умолчанию mongoexport поддерживает json/csv, но, к сожалению, в csv по какой-то причине экспортировать коллекцию не удалось. Ок, будем двигаться дальше с json! Экспорт в него, потом cd /var/www и скопировать файл в него, чтобы можно было скачать для работы локально.

Следующий вызов &#8211; как из JSON получить список email  адресов, ведь &#8220;чистым&#8221; этот файл не назовешь. Пытаюсь через Google Sheets, но из-за того, что в файле были и пустые поля для email  адресов, то скрипт (<https://github.com/bradjasper/ImportJSON>) не хотел работать. Начинаю &#8220;чистить&#8221; файл руками в Sublime Text и нахожу параллельно Pretty JSON для Subline (<https://blog.adriaan.io/sublime-pretty-json.html>). Теперь уже намного лучше, но все равно не идеально. Еще часик работы с сортировкой по алфавиту, чтобы выловить лишнюю инфо и текстовый файлик на 150 кб готов, а клиент приятно удивлен.