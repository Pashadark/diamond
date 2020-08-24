# Импорты
import telebot
from telebot import types
#Главное меню
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('✂Барбер')
#Главное меню
admin = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
admin.row('/time', '/static')
admin.row('Админы', '❌Обратно')
#Барбер меню
barber = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
barber.row('Тигран')
barber.row('Алексей')
barber.row('Антон')
barber.row('Гаянэ')
# Сервис меню 1
service1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = types.KeyboardButton('Мужская стрижка')
itembtn2 = types.KeyboardButton('Стрижка ножницами')
itembtn3 = types.KeyboardButton('Детская стрижка')
itembtn4 = types.KeyboardButton('Отец+Сын')
itembtn5 = types.KeyboardButton('Мужская стрижка+бритье')
itembtn55 = types.KeyboardButton('Стрижка машинкой')
itembtn6 = types.KeyboardButton('Окантовка')
itembtn7 = types.KeyboardButton('Ничего')
service1.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn55, itembtn6, itembtn7)
# Сервис меню 2
service2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn8 = types.KeyboardButton('Моделирование бороды')
itembtn9 = types.KeyboardButton('Стрижка бороды и усов')
itembtn10 = types.KeyboardButton('Камуфляж бороды')
itembtn11 = types.KeyboardButton('Окантовка')
itembtn12 = types.KeyboardButton('Ничего')
service2.add(itembtn8, itembtn9, itembtn10, itembtn11, itembtn12)
# Сервис меню 3
service3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn13 = types.KeyboardButton('Черная маска')
itembtn14 = types.KeyboardButton('Коррекция бровей')
itembtn15 = types.KeyboardButton('Мытье и укладка волос')
itembtn16 = types.KeyboardButton('Камуфляж головы')
itembtn17 = types.KeyboardButton('Чистка лица')
itembtn18 = types.KeyboardButton('Патчи')
itembtn19 = types.KeyboardButton('Удаление волос в носу')
itembtn20 = types.KeyboardButton('Ничего')
service3.add(itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19, itembtn20)

keyboardhelp = telebot.types.InlineKeyboardMarkup()
keyboardhelp.add(telebot.types.InlineKeyboardButton('Написать разработчику', url='telegram.me/pashadark'))



