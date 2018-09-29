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


  
if True:
 #try:
   print('7777')
   x=users.find({})
   for ids in x:
      bot.send_message(ids['id'], 'Бот был перезагружен! Возможно, вышло обновление.')
   bot.polling(none_stop=True,timeout=600)
 #except:
 #       print('!!! READTIME OUT !!!') 
 #       try:
 #          bot.stop_polling()
 #       except:
 #          pass
 #       time.sleep(1)
 #       check = True
 #       while check==True:
 #         try:
 #           bot.polling(none_stop=True,timeout=1)
 #           print('checkkk')
 #           check = False
 #         except:
 #           time.sleep(1)
   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(0.1)
