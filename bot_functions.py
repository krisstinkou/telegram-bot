import random
import os
import datetime


def coin_toss():
    """
    Функция, реализующая бросок монетки.
    :return: рехультат броска.
    """
    return random.choice(['Орёл!', 'Решка!'])


def print_console_log(message):
    """
    Функция вывода логов сообзения в консоль.
    :param message: сообщение, присланное пользователем.
    """
    print('Chat ID: ', message.chat.id)
    print('Username: ', message.chat.username)
    print('First name: ', message.chat.first_name)
    print('Last name: ', message.chat.last_name)
    print('Text: ', message.text)
    print('-' * 30)


def write_log(message):
    """
    Функция записи логов в файл. Создаётся папка с id пользователя (в Telegram), в папке создаётся файл
    log.txt, в который записываются все принятые сообщения от пользователя вместе с текущим временем и
    юзернеймом пользвователя в Telegram. Если пользователь уже писал боту ранее, папка не создаётся.
    :param message: сообщение, присланное пользователем.
    """
    try:
        os.mkdir(str(message.chat.id))
    except FileExistsError:
        pass
    current_time = datetime.datetime.now()
    path = os.getcwd() + "\\" + str(message.chat.id)
    if message.content_type == 'text':
        with open(path + '\\log.txt', 'a', encoding='utf-8') as file:
            file.write(f"{current_time}, {message.chat.username}: {message.text}\n")
