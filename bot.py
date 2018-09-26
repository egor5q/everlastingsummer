# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize



from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


@bot.message_handler(commands=['start'])
def start(m):
  if m.from_user.id==m.chat.id:
    if users.find_one({'id':m.from_user.id})==None:
        users.insert_one(createuser(m.from_user.id, m.from_user.first_name))
        bot.send_message(m.chat.id, 'Вы создали аккаунт! Добро пожаловать в бота!') 
    else:
        bot.send_message(m.chat.id, 'Бот работает!')
  
  
def createuser(id, name):
    return{'id':id,
           'name':name
          }

    
  
if True:
 try:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
 except:
        print('!!! READTIME OUT !!!') 
        try:
           bot.stop_polling()
        except:
           pass
        time.sleep(1)
        check = True
        while check==True:
          try:
            bot.polling(none_stop=True,timeout=1)
            print('checkkk')
            check = False
          except:
            time.sleep(1)
   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(0.1)
