# Прикрутить телеграм бота к задаче "Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования".

## Команда

[Александр Колибаба (тимлид)](https://gb.ru/users/4281457)

[Александр Захаров](https://gb.ru/users/5361206)

[Александр Кошин](https://gb.ru/users/7772942)

## Подготовка к запуску

1. Скачать репозиторий на локальный компьютер.

2. Установить библиотеку **pyTelegramBotAPI**: <code>pip install pyTelegramBotAPI</code>.

3. Установить библиотеку **python-dotenv**: <code>pip install python-dotenv</code>.

4. Создать файл <code>.env</code> с содержимым <code>TOKEN='\<your token\>'</code>.

## Запуск

1. Запуск программмы производится из файла <code>bot.py</code>.

2. Для старта калькулятора в Telegram нужно ввести команду <code>/start</code> или команду <code>/calculater</code>.

## Примечание

Соединение с ботом подтормаживает. Для корректной работы калькулятора нужно вводить данные размеренно, не спеша.

## Примечание 2

Прикрутить комплексные числа к стандартному калькулятору оказалось нетривиальной задачей. Наверняка что-то не учтено. Но основной функционал работает.