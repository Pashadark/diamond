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
# Классы
# предварительно создаем переменную psw ( рандомное число )
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


user_dict = {}


# Классы
class User:
    def __init__(self, category):
        self.category = category

        keys = ['fullname', 'phone', 'address', 'message', 'end', 'serial']

        for key in keys:
            self.key = None

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
        '1) Если бот завис и не работает нажмите /start.\n' +
        '2) Если у вас есть предложение напишите мне.\n' +
        '3) Список команд нажмите /commands \n',
        reply_markup=keyboard.keyboardhelp)


@bot.message_handler (commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я пока в тестовом режиме работаю. \nБудут проблемы нажми /help', reply_markup=keyboard.keyboard1)
    bot.send_chat_action (message.chat.id, 'typing')
    time.sleep(1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAINkl7AH2HI5BFg7fTaSd5cvBR67-hOAAKMCAACeVziCYUNIF_-rII7GQQ')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '✂Барбер':
        msg = bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=keyboard.barber)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        bot.register_next_step_handler(msg, process_category_step)
def process_category_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите услугу оказанную мастером', reply_markup=keyboard.service)
        bot.register_next_step_handler(msg, process_end_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_end_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.end = message.text

        # Говорим о создании заявки
        bot.send_message(chat_id, getRegData(user, 'Мы все учли, отправляем...', message.from_user.first_name),
                          parse_mode="Markdown", reply_markup=keyboard.keyboard1)
        bot.send_message(message.chat.id, 'Готово', reply_markup=keyboard.keyboard1)
        # Отправляем в группу
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(config.chat_id, getRegData(user, 'Оповещение от', bot.get_me ().username),
                          parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


# Формирует вид заявки регистрации
def getRegData(user, title, name):
    t = Template(
        '$title *$name* \n\n 🧔Барбер: *$category* \n ✂Услуга: *$end* \n ⌚Дата: *$data*')

    return t.substitute({
        'title': title,
        'name': name,
        'category': user.category,
        'end': user.end,
        'data': now.strftime("%d-%m-%Y %H:%M")
    })
    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers (delay=2)

    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers ()
    
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'NumberOne':
    bot.send_message(c.message.chat.id, 'Это кнопка 1')
  if c.data == 'NumberTwo':
    bot.send_message(c.message.chat.id, 'Это кнопка 2')
  if c.data == 'NumberTree':
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
    key.add(but_1, but_2, but_3)
    bot.send_message(c.message.chat.id, 'Это кнопка 3', reply_markup=key)


# Ребут после ошибки
while True:
    try:
        bot.polling(none_stop=True)
    except:
        print('Ошибка! Пробую востановить сервер...')
        time.sleep (1)
        print('Загрузка... █ 15%')
        time.sleep (1)
        print('Загрузка... ███ 30%')
        time.sleep (1)
        print('Загрузка... ██████ 45%')
        time.sleep (1)
        print('Загрузка... █████████ 60%')
        time.sleep (1)
        print('Загрузка... ████████████ 100%')
        time.sleep (4)
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(4)
