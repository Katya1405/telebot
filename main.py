import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup as b

TOKEN = '6021153829:AAFXbqWAZyqHiJPg2tGj4ASBSY8KMlWXwAw'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def view(message):
    mess = f'Привет, {message.from_user.first_name}, рад тебя видеть! Если захочешь посмотреть товары с лучшими скидками, выбери нужную категорию ниже!'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['start'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    electronics = types.KeyboardButton('Электроника')
    consols = types.KeyboardButton('Консоли и видеоигры')
    home = types.KeyboardButton('Дом и квартира')
    fashion = types.KeyboardButton('Мода')
    health = types.KeyboardButton('Здоровье и красота')
    travels = types.KeyboardButton('Путешествия')
    sport = types.KeyboardButton('Спорт и активный отдых')
    markup.add(electronics, consols, home, fashion, health, travels, sport)
    bot.send_message(message.chat.id,'Выбери одну из категорий ниже',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def operations(message):
    bot.send_message(message.chat.id, 'Здесь можно найти все самые выгодные предложения по твоей категории')
    if message.text == 'Электроника':
        bot.send_message(message.chat.id, 'https://www.pepper.ru/groups/electronics', disable_web_page_preview=1)
    elif message.text == 'Консоли и видеоигры':
        bot.send_message(message.chat.id, 'https://www.pepper.ru/groups/gaming', disable_web_page_preview=1)
    elif message.text == 'Дом и квартира':
        bot.send_message(message.chat.id, 'https://www.pepper.ru/groups/home-and-garden', disable_web_page_preview=1)
    elif message.text == 'Мода':
        bot.send_message(message.chat.id, 'https://www.pepper.ru/groups/fashion', disable_web_page_preview=1)
    elif message.text == 'Здоровье и красота':
        bot.send_message(message.chat.id,'https://www.pepper.ru/groups/health-beauty', disable_web_page_preview=1)
    elif message.text == 'Путешествия':
        bot.send_message(message.chat.id, 'https://www.pepper.ru/groups/travel', disable_web_page_preview=1)
    elif message.text == 'Спорт и активный отдых':
        bot.send_message(message.chat.id, 'https://www.pepper.ru/groups/sports', disable_web_page_preview=1)

bot.polling(none_stop=True)

