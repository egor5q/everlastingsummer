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

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

client1=os.environ['database']
client=MongoClient(client1)
db=client.worldseer
humans=db.humans
users=db.users

@bot.message_handler(commands=['start'])
def start(m):
  if m.from_user.id==m.chat.id:
    if users.find_one({'id':m.from_user.id})==None:
        users.insert_one(createuser(m.from_user.id, m.from_user.first_name))
        bot.send_message(m.chat.id, '''Вы создали аккаунт! Добро пожаловать в бота!\n\n
        В этой игре вы будете исполнять роль внутреннего голоса различных людей... 
        Агел, Бог, Дьявол - называйте себя как вам угодно. Вам предлагается принимать участие в жизни людей, подсказывать им, 
        как поступить.
        Живут все эти люди в обычном Российском городе, можете сами придумать ему название. Случайные знакомства, 
        трудоустройство, решение житейских проблем - в общем, всё, как в обычной жизни. Вы спросите: "А что мне с этого?", верно?
        За помощь в принятии решений вы будете получать Силы Создателя! О как красиво звучит... На них вы 
        сможете создавать своих собственных людей с выбранными вами характеристиками, и получать информацию о них в любой момент.
        Бывало ведь такое, когда вам казалось, что Бог не дал вам достаточно удачи, например, при создании? Или, например, 
        красоты... Может быть, вы тоже находитесь в игре, и Он просто экспериментировал :) В общем, у вас тоже будет 
        возможность поэкспериментировать с характеристиками людей в этом мире и наблюдать, что из этого выйдет) Удачи!
        ''') 
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
         'sociality':random.randint(1,1000),
         'luck':random.randint(1,1000),
         'happy':random.randint(1,1000),
         'age':random.randint(18,100),
         'old':random.randint(1,1000),
         'diligence':random.randint(1,1000),     # Трудолюбивость
         'gameskill':random.randint(1,1000),
         'sportsman':random.randint(1,1000),
         'attentiveness':random.randint(1,1000), # Внимательность
         'creativity':random.randint(1,1000),    # Креативность
         'beautiful':random.randint(1,1000),     # Красота
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
