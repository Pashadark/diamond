#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################
# Telegram bot Diamond version 0.0.1   #
# programming and created by @pashadark#
########################################

# Импорты
import sys
import telebot
from telebot import types
import time
import config
import keyboard
import logging
from string import Template

import requests
import datetime

# Токены
bot = telebot.TeleBot(config.token)
now = datetime.datetime.now()


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

named_tuple = time.localtime() # получить struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# Классы
user_dict = {}


class User:
    def __init__(self, category):
        self.category = category

        keys = ['fullname', 'phone', 'address', 'message', 'head', 'beard']

        for key in keys:
            self.key = None


### Функция проверки авторизации
def autor(chatid):
    strid = str(chatid)
    for item in config.users:
        if item == strid:
            return True
    return False


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                      '1) Если бот завис и не работает нажмите /start\n' +
                      '2) Команды для администратора /admin\n' +
                      '3) Список команд нажмите /commands\n' +
                      '4) Время и дата на сервере /time \n' +
                      '5) Если у вас есть предложение напишите мне⤵',
                      reply_markup=keyboard.keyboardhelp)


@bot.message_handler(commands=['time'])
def time_command(message):
    bot.send_message(message.chat.id, 'Время и дата на сервере\n' + now.strftime("%m/%d/%Y, %H:%M:%S"))

bot.message_handler (commands=['list'])
def list_command(message):
    bot.send_message(message.chat.id, 'Список администраторов')



@bot.message_handler (commands=['admin'])
def start_message(message):
    if autor(message.chat.id):
        cid = message.chat.id
        message_text = message.text
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        # mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        bot.send_message(message.chat.id, 'Привет администратор', reply_markup=keyboard.admin)
        bot.send_message(message.chat.id, 'Вот пару команд для тебя', reply_markup=keyboard.admin)
    else:
        bot.send_message(message.chat.id,
                          'Вы не являетесь администратором для выполнения этой команды' + str (message.chat.id))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я пока в тестовом режиме работаю. \nБудут проблемы нажми /help',
                      reply_markup=keyboard.keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '✂Барбер':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=keyboard.barber)
        bot.register_next_step_handler(msg, process_category_step)

def process_category_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите услугу 1', reply_markup=keyboard.service1)
        bot.register_next_step_handler(msg, process_head_step)

    except Exception as e:
        bot.reply_to(message, 'Ой что-то не то!!')

def process_head_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.head = message.text
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите услугу 2', reply_markup=keyboard.service2)
        bot.register_next_step_handler(msg, process_beard_step)

    except Exception as e:
        bot.reply_to(message, 'Ой что-то не то!!')


def process_beard_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.beard = message.text
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите услугу 3', reply_markup=keyboard.service3)
        bot.register_next_step_handler(msg, process_end_step)

    except Exception as e:
        bot.reply_to(message, 'Ой что-то не то!!')


def process_end_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.end = message.text

        # Говорим о создании заявки
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        bot.send_message(chat_id, getRegData(user, 'Мы все учли, отправляем...', message.from_user.first_name),
                          parse_mode="Markdown")
        time.sleep(2)
        bot.send_message(message.chat.id, 'Готово', reply_markup=keyboard.keyboard1)
        # Отправляем в группу
        bot.send_message(config.chat_id, getRegData(user, 'Оповещение от', bot.get_me().username),
                          parse_mode="Markdown")


    except Exception as e:
        bot.reply_to(message, 'Ой что-то не то!!')


# Формирует вид заявки регистрации
def getRegData(user, title, name):
    t = Template(
        '$title *$name* \n\n 🧔Барбер: *$category* \n\n ✂Голова: *$head* \n ✂Борода: *$beard* \n ✂Лицо: *$end* \n ⌚Дата: *$data*')

    return t.substitute({
        'title': title,
        'name': name,
        'category': user.category,
        'head': user.head,
        'beard': user.beard,
        'end': user.end,
        'data': now.strftime("%m/%d/%Y")
    })
    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers (delay=2)

    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers ()

@bot.callback_query_handler (func=lambda c: True)
def inline(c):
    if c.data == 'NumberOne':
        bot.send_message (c.message.chat.id, 'Это кнопка 1')
    if c.data == 'NumberTwo':
        bot.send_message (c.message.chat.id, 'Это кнопка 2')
    if c.data == 'NumberTree':
        key = types.InlineKeyboardMarkup ()
        but_1 = types.InlineKeyboardButton (text="NumberOne", callback_data="NumberOne")
        but_2 = types.InlineKeyboardButton (text="NumberTwo", callback_data="NumberTwo")
        but_3 = types.InlineKeyboardButton (text="NumberTree", callback_data="NumberTree")
        key.add(but_1, but_2, but_3)
        bot.send_message(c.message.chat.id, 'Это кнопка 3', reply_markup=key)


# Ребут после ошибки
while True:
    try:
        bot.polling(none_stop=True)
    except:
        print('Ошибка! Пробую востановить сервер...')
        time.sleep(1)
        print('Загрузка... █ 15%')
        time.sleep(1)
        print('Загрузка... ███ 30%')
        time.sleep(1)
        print('Загрузка... ██████ 45%')
        time.sleep (1)
        print('Загрузка... █████████ 60%')
        time.sleep (1)
        print('Загрузка... ████████████ 100%')
        time.sleep(4)
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(4)
