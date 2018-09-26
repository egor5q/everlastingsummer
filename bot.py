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
  
@bot.message_handler(commands=['myhuman'])
def myhuman(m):
  if m.from_user.id==m.chat.id:
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
      if x['currenthuman']!=None:
        y=humans.find_one({'id':x['currenthuman']})
        if y!=None:
          bot.send_message(m.chat.id, 'Информация о человеке с именем "*'+y['name']+'*":\n\n'+
                           'Наличные: '+str(y['currentmoney'])+'\n'+
                           'Дом: '+housetotext(y['house'])+'\n'+
                           'Социальность: '+str(y['sociality'])+'\n'+
                           'Удача: '+str(y['luck'])+'\n'+
                           'Счастье: '+str(y['happy'])+'\n'+
                           'Возраст: '+str(y['age'])+'\n'+
                           'Здоровье: '+str(y['health'])+'\n'+
                           'Трудолюбивость: '+str(y['diligence'])+'\n'+
                           'Скилл в компьютерных играх: '+str(y['gameskill'])+'\n'+
                           'Любовь к спорту: '+str(y['sportsman'])+'\n'+
                           'Внимательность: '+str(y['attentiveness'])+'\n'+
                           'Креативность: '+str(y['creativity'])+'\n'+
                           'Внешняя привлекательность: '+str(y['beautiful'])+'\n'+
                           'Пол: '+gendertotext(y['gender'])+'\n'+
                           'Ориентация: '+gaytotext(y['gay'])+'\n'+
                           'Личный идентефикатор: '+str(y['id'])+'\n'+
                           'Кто в данный момент следит за человеком: '+idtoname(y['innervoice'])+'\n'+
                           'Кто создал человека: '+creatortotext(y['creator'])
                          )
          
          
     
def gendertotext(gender):
  if gender=='male':
    return 'Мужчина'
  elif gender=='female':
    return 'Женщина'
  
def gaytotext(gay):
  if gay==1:
    return 'Нетрадиционная'
  elif gay==0:
    return 'Традиционная'
  

  
  
@bot.message_handler(commands=['humansinfo'])
def humansinfo(m):
  if m.from_user.id==441399484:
    x=humans.find({})
    bot.send_message(m.chat.id, 'Количество человек, проживающих в городе: '+str(len(x))+'!')

@bot.message_handler(commands=['createhumans'])
def createhumans(m):
  if m.from_user.id==441399484:
    x=0
    while x<100:
      humans.insert_one(createhuman('world'))
      x+=1
    bot.send_message(m.chat.id, '100 человек успешно созданы и в данный момент проживают в городе!')



def createuser(id, name):
    return{'id':id,
           'name':name,
           'currenthuman':None,
           'godpower':0
          }
  
malenames=['Пётр','Александр','Василий','Иван','Борис','Вячеслав','Леонид','Георгий','Юрий','Николай','Илья','Даниил','Максим','Виктор',
           'Никита','Артём','Игорь','Денис','Матвей','Сергей']
femalenames=['Алиса','Мария','Александра','Лена','Ульяна','Ангелина','Вероника','Дарья','Диана','Елена','Ксения','Лина','Олеся',
             'Полина','Софья','Татьяна','Юлия','Марта','Марина','Светлана']
genders=['male', 'female']
  
houses=['self',  'rental'] 
                 # Съемная
def createhuman(creator):
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
  id=random.randint(1,1000000)
  humanlist=humans.find({})
  humanids=[]
  for ids in humanlist:
    humanids.append(ids['id'])
  while id in humanids:
    id=random.randint(1,1000000)
  return{'name':random.choice(genderlist),
         'acting':0,
         'currentmoney':random.randint(0,1000000),
         'house':random.choice(houses)
         'sociality':random.randint(1,1000),
         'luck':random.randint(1,1000),
         'happy':random.randint(1,1000),
         'age':random.randint(18,100),
         'old':random.randint(1,1000),
         'friends':[],
         'love':None,
         'health':random.randint(1,1000),
         'diligence':random.randint(1,1000),     # Трудолюбивость
         'gameskill':random.randint(1,1000),
         'sportsman':random.randint(1,1000),
         'attentiveness':random.randint(1,1000), # Внимательность
         'creativity':random.randint(1,1000),    # Креативность
         'beautiful':random.randint(1,1000),     # Красота
         'gender':gender,
         'gay':gay,
         'id':id,                                # Уникальный индекс человека
         'innervoice':None,                      # Внутренний голос: айди наблюдающего за человеком
         'creator':creator                       # Айди бога, создавшего этого человека
        }
         

def life():
  t=threading.Timer(1, life)     # 1 секунда реальной жизни равна одной минуте в городе
  t.start()
  
  x=humans.find({})
  for ids in x:
    if ids['acting']==0:
      human.actfind(ids)
    
  
   
if True:
  life()
    
    
  
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
