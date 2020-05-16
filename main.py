#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

# Токены
bot = telebot.TeleBot(config.token)

# Логи
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

# Тут работаем с командой /start
@bot.message_handler(commands=['start'])
def command_hello(message):
    bot.reply_to(message, "Привет, если вы видите это сообщение, значит я работаю так, как надо🤩", markup=keyboard.keyboard1)

# Тут работаем с командой /help
@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Чем я могу тебе помочь?')

@bot.message_handler(commands=['ping'])
def ping(message):

    nowtime = time.time()
    uptime = round(nowtime - runtime)
    uptimestr = str(time.strftime("%H:%M:%S", time.gmtime(int(uptime))))
    answertime = nowtime - message.date
    nowtimestr = time.ctime(nowtime)
    status = bot.get_webhook_info().pending_update_count - 1
    msgg = bot.reply_to(message,'Текущее время: '+ str(nowtimestr) + '\nБот ответил за: ' + str(answertime) + '\n Бот активен уже: ' + str(uptimestr)  + '\nСообщений в очереди: ' + str(status),  parse_mode='html')


@bot.message_handler(commands=['barber'])
def user_reg(message):
    msg = bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=keyboard.barber)
    bot.register_next_step_handler(msg, process_category_step)


def process_category_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User (message.text)
        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove (selective=False)

        msg = bot.send_message (message.chat.id, 'Выберите услугу оказанную мастером', reply_markup=keyboard.service)
        bot.register_next_step_handler (msg, process_end_step)

    except Exception as e:
        bot.reply_to (message, 'ooops!!')


def process_end_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.end = message.text

        # ваша заявка "Имя пользователя"
        bot.send_message (chat_id, getRegData (user, 'Мы все учли, отправляем...', message.from_user.first_name),
                          parse_mode="Markdown", reply_markup=keyboard.keyboard1)
        # отправить в группу
        bot.send_message (config.chat_id, getRegData (user, 'Оповещение от', bot.get_me ().username),
                          parse_mode="Markdown")

    except Exception as e:
        bot.reply_to (message, 'ooops!!')


# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template (
        '$title *$name* \n\n Барбер: *$category* \n Услуга: *$end*')

    return t.substitute ({
        'title': title,
        'name': name,
        'category': user.category,
        'end': user.end,
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
        bot.polling (none_stop=True)
    except:
        print ('Ошибка! Пробую востановить сервер...')
        time.sleep (1)
        print ('1')
        time.sleep (1)
        print ('2')
        time.sleep (1)
        print ('3')
        time.sleep (1)
        print ('4')
        time.sleep (1)
        print ('5')
        time.sleep (1)
        logging.error ('error: {}'.format (sys.exc_info ()[0]))
        time.sleep (3)
