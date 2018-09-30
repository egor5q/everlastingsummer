# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

client1=os.environ['database']
client=MongoClient(client1)
db=client.worldseer
users=db.users


@bot.message_handler(commands=['start'])
def start(m):
 if m.chat.id==m.from_user.id:
  kb=types.InlineKeyboardMarkup()
  kb.add(types.InlineKeyboardButton(text='Свет', callback_data='radiant'))
  kb.add(types.InlineKeyboardButton(text='Тьма', callback_data='dire'))
  bot.send_message(m.chat.id, 'Какую сторону выберешь?')
  


  
if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)

