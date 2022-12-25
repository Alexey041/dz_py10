import telebot
import random
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

def apology(mes):
    num = random.randint(1,5)
    user_num = int(mes.text)
    print(num)
    if user_num != num:
        bot.send_message(mes.chat.id, 'Не угодал!')
    if user_num == num:
        bot.send_message(mes.chat.id, 'Угодал!')

def text_open(search_str):
    with open('text.txt', 'r', encoding='utf8') as text:
        find_str = text.read().split(';')
    return find_str[search_str]
        
        
"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Покормить абрикосика')
    item2 = telebot.types.KeyboardButton('Пнуть сенцовчанина')
    item3 = telebot.types.KeyboardButton('Знаки зодиака')
    item4 = telebot.types.KeyboardButton('Извинись')


    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Хай, зяблы! Жмых эйрайнс приветстуют вас!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет' or message.text == 'Привет':
        bot.send_message(message.chat.id, 'Борт две двоечки, одна восьмерочка приветствует Вас!')
    elif message.text == 'Покормить абрикосика':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxUAAWOkSTggaoPNlcmkRnD9hbHorHRiAAJvAAPANk8TlzojknPv81gsBA')
    elif message.text == 'Пнуть сенцовчанина':
        photo = open('photo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif message.text == 'Знаки зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        item4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item9 = telebot.types.InlineKeyboardButton('Змееносец', callback_data='Змееносец')
        item10 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item11 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item12 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item13 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

        bot.send_message(message.chat.id, 'ИЗВЕНИСЬ БЫСТРО!!', reply_markup=markup)

    elif message.text == 'Извинись':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('За шо?', callback_data='10')
        item2 = telebot.types.InlineKeyboardButton('Извини', callback_data='20')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'ИЗВЕНИСЬ БЫСТРО!!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'АСУЖДАЮ!!!')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '10':
        video = open('video.mp4', 'rb')
        bot.send_video(call.message.chat.id, video)
    if call.data == '20':       
        mes = bot.send_message(call.message.chat.id, 'Угадай сколько раз тебе извиниться')
        bot.register_next_step_handler(mes, apology)


    if call.data == 'Овен':
        search_str = 0
        bot.send_message(call.message.chat.id, text_open(search_str))   
    if call.data == 'Телец':
        search_str = 1
        bot.send_message(call.message.chat.id, text_open(search_str))       
    if call.data == 'Близнецы':
        search_str = 2
        bot.send_message(call.message.chat.id, text_open(search_str))  
    if call.data == 'Рак':
        search_str = 3
        bot.send_message(call.message.chat.id, text_open(search_str))  
    if call.data == 'Лев':
        search_str = 4
        bot.send_message(call.message.chat.id, text_open(search_str))   
    if call.data == 'Дева':
        search_str = 5
        bot.send_message(call.message.chat.id, text_open(search_str))       
    if call.data == 'Весы':
        search_str = 6
        bot.send_message(call.message.chat.id, text_open(search_str))  
    if call.data == 'Скорпион':
        search_str = 7
        bot.send_message(call.message.chat.id, text_open(search_str))  
    if call.data == 'Змееносец':
        search_str = 8
        bot.send_message(call.message.chat.id, text_open(search_str))   
    if call.data == 'Стрелец':
        search_str = 9
        bot.send_message(call.message.chat.id, text_open(search_str))       
    if call.data == 'Козерог':
        search_str = 10
        bot.send_message(call.message.chat.id, text_open(search_str))  
    if call.data == 'Водолей':
        search_str = 11
        bot.send_message(call.message.chat.id, text_open(search_str))  
    if call.data == 'Рыбы':
        search_str = 12
        bot.send_message(call.message.chat.id, text_open(search_str))   
 

bot.polling(none_stop=True)