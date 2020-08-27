#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################
# Telegram bot Diamond version 0.0.3   #
# programming and created by @pashadark#
########################################

# Импорты
import sys

import telebot
from telebot import types
import time
import datetime
import config
import keyboard
import logging
from string import Template
import tg_analytic
import datetime as DT
import pytz
import requests

# Включить ведение журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Токены
bot = telebot.TeleBot(config.token)
# Атрибуты
now = datetime.datetime.today()
# Классы
user_dict = {}


class User:
    def __init__(self, category):
        self.category = category

        keys = ['fullname', 'phone', 'address', 'message', 'head', 'beard']

        for key in keys:
            self.key = None

# Команды
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
    bot.send_message(message.chat.id, 'Привет администратор')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я пока в тестовом режиме работаю. \nБудут проблемы нажми /help',
                      reply_markup=keyboard.keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st,message.chat.id)
            with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
                bot.send_document(message.chat.id,file)
            tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st,message.chat.id)
            bot.send_message(message.chat.id, messages)

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
        tg_analytic.statistics (message.chat.id, message.text)
        bot.register_next_step_handler(msg, process_head_step)

    except Exception as e:
        bot.reply_to(message, '⚠ Ошибка, мы исправим')

def process_head_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.head = message.text
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите услугу 2', reply_markup=keyboard.service2)
        tg_analytic.statistics (message.chat.id, message.text)
        bot.register_next_step_handler(msg, process_beard_step)

    except Exception as e:
        bot.reply_to(message, '⚠ Ошибка, мы исправим')


def process_beard_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.beard = message.text
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        msg = bot.send_message(message.chat.id, 'Выберите услугу 3', reply_markup=keyboard.service3)
        tg_analytic.statistics (message.chat.id, message.text)
        bot.register_next_step_handler(msg, process_end_step)

    except Exception as e:
        bot.reply_to(message, '⚠ Ошибка, мы исправим')


def process_end_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.end = message.text

        # Говорим о создании заявки
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        bot.send_message(chat_id, getRegData(user, 'Собираем данные, отправляем...', message.from_user.first_name),
                          parse_mode="Markdown")
        time.sleep(2)
        bot.send_message(message.chat.id, 'Готово', reply_markup=keyboard.keyboard1)
        # Отправляем в группу
        bot.send_message(config.chat_id, getRegData(user, 'Оповещение от', bot.get_me().username),
                          parse_mode="Markdown")


    except Exception as e:
        bot.reply_to(message, '⚠Ошибка, мы исправим')


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
        'data': now.strftime("%d/%m/%Y")
    })
    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers (delay=2)

    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers ()

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
