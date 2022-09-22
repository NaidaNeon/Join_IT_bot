import os
import telebot

from secret import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['bot']) 
def call_bot(msg):
    bot.reply_to(msg, "Hello! \nПозвать админа на помощь введи /admin \nГлянуть вводное видео введи /video \nГлянуть библиотеку по Python введи /python \nГлянуть библиотеку по Java введи /java \nГлянуть библиотеку по остальным направлениям введи /library")


@bot.message_handler(commands=['admin']) 
def call_admin(msg):
    bot.send_message(msg.chat.id, '@HadesArchitect @semen67sml @scorp_dev_null')

@bot.message_handler(commands=['voiti']) 
def call_video(msg):
    bot.send_message(msg.chat.id, 'Глянь вводное видео https://youtu.be/jqLDmyquhnM')


@bot.message_handler(commands=['python']) 
def call_python(msg):
    bot.send_message(msg.chat.id, 'Ссылки на курсы по питончику')


@bot.message_handler(commands=['java']) 
def call_java(msg):
    bot.send_message(msg.chat.id, 'Ссылки на курсы по джаве')

@bot.message_handler(commands=['library']) 
def call_library(msg):
    bot.send_message(msg.chat.id, 'Ссылки на библиотеку ресурсов')

bot.polling()