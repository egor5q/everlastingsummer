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
    bot.send_message(m.chat.id,'Здраствуй, пионер! Впереди тебя ждёт интересная жизнь в лагере "Совёнок"! '+
                     'А сейчас скажи нам, как тебя зовут (следующим сообщением).')
  else:
    bot.send_message(m.chat.id, 'Бот работает!')
  

  
@bot.message_handler()
def messag(m):
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
        if x['setname']==1:
            users.update_one({'id':m.from_user.id},{'$set':
  
def createuser(id, name, username):
    return{'id':id,
           'name':name,
           'username':username,
           'pionername':None,
           'strenght':3,
           'agility':3,
           'intelligence':3,
           'setname':1
          }
    
    
    
if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)

