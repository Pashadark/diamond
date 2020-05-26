# Импорты
import telebot
from telebot import types
#Главное меню
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('✂Барбер')
#Главное меню
admin = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
admin.row('/time', '/list')
admin.row('Админы', '❌Обратно')
#Барбер меню
barber = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
barber.row('Тигран')
barber.row('Алексей')
barber.row('Антон')
# Сервис меню
service1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = types.KeyboardButton('Мужская стрижка')
itembtn2 = types.KeyboardButton('Стрижка ножницами')
itembtn3 = types.KeyboardButton('Детская стрижка')
itembtn4 = types.KeyboardButton('Отец+Сын')
itembtn5 = types.KeyboardButton('Стрижка под машинку')
itembtn6 = types.KeyboardButton('Мужская стрижка+бритье')
itembtn7 = types.KeyboardButton('Ничего')
service1.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)

service2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn7 = types.KeyboardButton('Стрижка бороды и усов')
itembtn8 = types.KeyboardButton('Моделирование бороды')
itembtn9 = types.KeyboardButton('Окантовка')
itembtn10 = types.KeyboardButton('Ничего')
service2.add(itembtn7, itembtn8, itembtn9, itembtn10)

keyboardhelp = telebot.types.InlineKeyboardMarkup()
keyboardhelp.add(telebot.types.InlineKeyboardButton('Написать разработчику', url='telegram.me/pashadark'))

key = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="1", callback_data="NumberOne")
but_2 = types.InlineKeyboardButton(text="2", callback_data="NumberTwo")
but_3 = types.InlineKeyboardButton(text="3", callback_data="NumberTree")
key.add(but_1, but_2, but_3)


