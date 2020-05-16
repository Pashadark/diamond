# Импорты
import telebot
from telebot import types
#Главное меню
keyboard1 = telebot.types.ReplyKeyboardMarkup (one_time_keyboard=True, resize_keyboard=True)
keyboard1.row ('/barber')
keyboard1.row ('🔑Аккаунт', '🏴‍Кнопка')
keyboard1.row ('🔩Команды', '❌Обратно')
#Барбер меню
barber = telebot.types.ReplyKeyboardMarkup (one_time_keyboard=True, resize_keyboard=True)
barber.row ('Тигран')
barber.row('Алексей')
barber.row('Антон')
# Сервис меню
service = types.ReplyKeyboardMarkup (one_time_keyboard=True, resize_keyboard=True)
itembtn1 = types.KeyboardButton ('Мужская стрижка')
itembtn2 = types.KeyboardButton ('Стрижка ножницами')
itembtn3 = types.KeyboardButton ('Стрижка бороды и усов')
itembtn4 = types.KeyboardButton ('Моделирование бороды')
itembtn5 = types.KeyboardButton ('Детская стрижка')
itembtn6 = types.KeyboardButton ('Отец+Сын')
itembtn7 = types.KeyboardButton ('Стрижка под машинку')
itembtn8 = types.KeyboardButton ('Камуфляж бороды')
itembtn9 = types.KeyboardButton ('Окантовка')
itembtn10 = types.KeyboardButton ('Мужская стрижка+бритье')
itembtn11 = types.KeyboardButton ('Удаление волос в носу с помощью теплого воска')
itembtn12 = types.KeyboardButton ('Коррекция бровей')
itembtn13 = types.KeyboardButton ('Мытьё и укладка волос')
service.add (itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13)