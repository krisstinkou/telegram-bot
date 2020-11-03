"""
Обработка фоток по фильтрам
Игра в угадай число
Игра в быки и коровы
Игра в крестики нолики
Генерация шутеечек
"""

"""
ЗАПУСК БОТА: 
Для запуска бота необходимо запустить main_file.py из консоли. Всё :)
Переход по папкам делается с помощью команды консоли:
            chdir <имя_папки>
Привет из 01.08.2020
"""

"""
Импорт файлов.
telebot - библиотека непосредственно для написания ботов для телеграмма на языке Python.
Документация: https://github.com/eternnoir/pyTelegramBotAPI
types - были проблемы с импортом клавиатуры, пришлось делать доп. импорт
bot_functions - чтобы не захламлять код, действия бота были вынесены в отдельный файл
"""

import telebot
from telebot import types
from bot_functions import coin_toss, print_console_log, write_log

# Инициализация бота
bot = telebot.TeleBot(YOUR_TOKEN)


# message.handler - принятие сообщений. Если пользователь отправил команду старт:
@bot.message_handler(commands=['start'])
def handle_start(message):
    print_console_log(message)  # вывод логов сообщения в консоль, из которой запущен бот
    write_log(message)  # в папке, где хранится файл бота, появляются папки и файлы с логами чатов
    # отправка сообщения пользователю
    bot.send_message(message.from_user.id, 'Привет! \
                                           Я тестовый бот для прогона всяких штук на Python. \
                                           Пока что ничего конкретного я не умею, но скоро обязательно научусь!\
                                           Введи /help или /menu, чтобы узнать обо мне побольше.')


# Если пользователь отправил команду menu, help
@bot.message_handler(commands=['menu', 'help'])
def handle_menu_help(message):
    # запись логов (см. строки 36-37) (ПОМЕНЯТЬ СТРОКИ ЕСЛИ БУДЕШЬ ДОПИСЫВАТЬ БОТА)
    print_console_log(message)
    write_log(message)
    # Если пользователь ввёл help - дополнительно вывести
    if message.text == '/help':
        # вот это вот сообщение
        bot.send_message(message.from_user.id, """
Я предназначен для тестирования, поэтому мои функции могут существенно меняться время от времени. \
Это нормально! Сейчас я в основном повторяю за тобой твои слова. НО! Есть у меня вот такие штуки: 
""")
    # Инициализация клавиатуры. Говорим, что будет клавиатура
    keyboard = types.InlineKeyboardMarkup()
    # Инициализация кнопки в меню (на клаве) с её идентификатором
    # text - надпись на кнопке
    # callback_data - что-то типа id кнопки. Данные, которые кнопка мониторит
    key_coin = types.InlineKeyboardButton(text='Бросок монетки', callback_data='coin')
    # Добавление кнопки на клавиатуру
    keyboard.add(key_coin)
    # Отправка сообщения с reply_markup - предложенной клавиатурой
    bot.send_message(message.from_user.id, 'Меню: ', reply_markup=keyboard)


# Мониторинг введёных кнопок. Берёт данные из кнопки и выполняет соотвествующую ветку цикла
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'coin':
        bot.send_message(call.message.chat.id, coin_toss())
    elif call.data == '':
        # TODO
        pass


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
# Функция для отправки эхо-сообщений
def echo_message(message):
    # Запись логов (см. строки 35-36)
    print_console_log(message)
    write_log(message)
    # Отправка сообщений с ответом на сообщение (reply_to), текст ответа - message.text - это
    # содержимое сообщения пользователя
    bot.reply_to(message, message.text)
    bot.send_message(message.from_user.id, 'Введи /help или /menu, чтобы узнать обо мне побольше')


# Зацикливание бота. none_stop=True - работает без передышки.
bot.polling(none_stop=True)
