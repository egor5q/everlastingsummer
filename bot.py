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


humans=db.humans
users=db.users

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
           'name':name,
           'currenthuman':None
          }
  
malenames=['Пётр','Александр','Василий','Иван','Борис','Вячеслав','Леонид','Георгий','Юрий','Николай','Илья','Даниил','Максим','Виктор',
           'Никита','Артём','Игорь','Денис','Матвей','Сергей']
femalenames=['Алиса','Мария','Александра','Лена','Ульяна','Ангелина','Вероника','Дарья','Диана','Елена','Ксения','Лина','Олеся',
             'Полина','Софья','Татьяна','Юлия','Марта','Марина','Светлана']
genders=['male', 'female']
  
  
def createhuman():
  gender=random.choice(genders)
  if gender=='male':
    genderlist=malenames
  elif gender=='female':
    genderlist=femalenames
  gay=random.randint(1,100)
  if gay<=10:
    gay=1
  else:
    gay=0
  id=random.randint(1,100000)
  humanlist=humans.find({})
  humanids=[]
  for ids in humanlist:
    humanids.append(ids['id'])
  while id in humanids:
    id=random.randint(1,100000)
  return{'name':random.choice(genderlist),
         'sociality':random.randint(1,100),
         'luck':random.randint(1,100),
         'happy':random.randint(1,100),
         'age':random.randint(18,100),
         'old':random.randint(1,100),
         'diligence':random.randint(1,100),     # Трудолюбивость
         'gameskill':random.randint(1,100),
         'sportsman':random.randint(1,100),
         'attentiveness':random.randint(1,100), # Внимательность
         'creativity':random.randint(1,100),    # Креативность
         'gender':gender,
         'gay':gay,
         'id':id
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
