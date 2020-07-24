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
barber.row('Гаянэ')
# Сервис меню
service1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = types.KeyboardButton('Мужская стрижка')
itembtn2 = types.KeyboardButton('Стрижка ножницами')
itembtn3 = types.KeyboardButton('Детская стрижка')
itembtn4 = types.KeyboardButton('Отец+Сын')
itembtn5 = types.KeyboardButton('Мужская стрижка+бритье')
itembtn6 = types.KeyboardButton('Ничего')
service1.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

service2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn7 = types.KeyboardButton('Моделирование бороды')
itembtn8 = types.KeyboardButton('Стрижка бороды и усов')
itembtn9 = types.KeyboardButton('Камуфляж бороды')
itembtn10 = types.KeyboardButton('Окантовка')
itembtn11 = types.KeyboardButton('Ничего')
service2.add(itembtn7, itembtn8, itembtn9, itembtn10, itembtn11)

service3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn12 = types.KeyboardButton('Черная маска')
itembtn13 = types.KeyboardButton('Коррекция бровей')
itembtn14 = types.KeyboardButton('Мытье и укладка волос')
itembtn15 = types.KeyboardButton('Камуфляж головы')
itembtn16 = types.KeyboardButton('Ничего')
service3.add(itembtn12, itembtn13, itembtn14, itembtn15, itembtn16)

keyboardhelp = telebot.types.InlineKeyboardMarkup()
keyboardhelp.add(telebot.types.InlineKeyboardButton('Написать разработчику', url='telegram.me/pashadark'))



