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
db=client.dotachat
users=db.users


@bot.message_handler(commands=['start'])
def start(m):
 if m.chat.id==m.from_user.id:
  if users.find_one({'id':m.from_user.id})==None:
    users.insert_one(createuser(m.from_user.id, m.from_user.first_name, m.from_user.username))
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Свет', callback_data='radiant'))
    kb.add(types.InlineKeyboardButton(text='Тьма', callback_data='dire'))
    bot.send_message(m.chat.id, 'Здраствуй! Ты попал на поле бесконечной битвы, где герои возрождаются снова и снова только для того, '+
                    'чтобы выяснить: кто же сильнее? Свет или Тьма? Вам предстоит выбрать, за кого будете сражаться.')
  else:
    bot.send_message(m.chat.id, 'Бот работает!')
  

def createuser(id, name, username):
    return{'id':id,
           'name':name,
           'username':username,
           'team':None,
           'gold':0,
           'hero':None
          }
    
    
    
if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)

