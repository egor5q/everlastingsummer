# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import humanacts
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
citytime=db.citytime

timee=citytime.find_one({})
year=timee['year']
month=timee['month']
day=timee['day']
hour=timee['hour']
minute=timee['minute']



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
                           'Наличные: '+str(y['variables']['currentmoney'])+'\n'+
                           'Дом: '+housetotext(y['variables']['house'])+'\n'+
                           'Социальность: '+str(y['sociality'])+'\n'+
                           'Удача: '+str(y['luck'])+'\n'+
                           'Счастье: '+str(y['happy'])+'\n'+
                           'Возраст: '+str(y['variables']['age'])+'\n'+
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
                           'Кто в данный момент следит за человеком: '+idtoname(y['variables']['innervoice'])+'\n'+
                           'Кто создал человека: '+creatortotext(y['creator'])
                          )
          
  
@bot.message_handler(commands=['clear'])
def clearr(m):
  humans.update_many({},{'$unset'})
  
     
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
  


@bot.message_handler(commands=['currentdate'])
def currentdate(m):
  global year
  global month
  global day
  global hour
  global minute
  bot.send_message(m.chat.id, 'Текущая дата в городе:\n'+
                   'Год: '+str(year)+'\n'+
                   'Месяц: '+monthtotext(month)+'\n'+
                   'День: '+str(day)+'\n'+
                   'Час: '+str(hour)+'\n'+
                   'Минута: '+str(minute)+'\n')
  
def monthtotext(month):
  if month==1:
    return 'Январь'
  elif month==2:
    return 'Февраль'
  elif month==3:
    return 'Март'
  elif month==4:
    return 'Апрель'
  elif month==5:
    return 'Май'
  elif month==6:
    return 'Июнь'
  elif month==7:
    return 'Июль'
  elif month==8:
    return 'Август'
  elif month==9:
    return 'Сентябрь'
  elif month==10:
    return 'Октябрь'
  elif month==11:
    return 'Ноябрь'
  elif month==12:
    return 'Декабрь'
                   
                   
                   
                   
@bot.message_handler(commands=['humansinfo'])
def humansinfo(m):
  if m.from_user.id==441399484:
    x=humans.find({})
    bot.send_message(m.chat.id, 'Количество человек, проживающих в городе: '+str(len(x))+'!')

@bot.message_handler(commands=['createhumans'])
def createhumans(m):
  if m.from_user.id==441399484:
    x=0
    while x<50:
      humans.insert_one(createhuman('world'))
      x+=1
    bot.send_message(m.chat.id, '100 человек успешно созданы и в данный момент проживают в городе!')


@bot.message_handler(commands=['watchhuman'])
def watchhuman(m):
  x=users.find_one({'id':m.from_user.id})
  if x!=None:
   if x['currenthuman']==None:
    y=[]
    z=humans.find({})
    for ids in z:
      if ids['variables']['age']<=22 and ids['variables']['seer']==None:
        y.append(ids)
    if len(y)>0:
      human=random.choice(y)
      users.update_one({'id':m.from_user.id},{'$set':{'currenthuman':human['id']}})
      humans.update_one({'id':human['id']},{'$set':{'variables.seer':m.from_user.id}})
      bot.send_message(m.chat.id, 'Теперь вы наблюдаете за человеком с именем '+human['name']+'... '+
                       'Его уникальный номер - '+str(human['id']))
   else:
    bot.send_message(m.chat.id, 'Вы уже наблюдаете за одним человеком!')
   
    
    
    
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
         'sociality':random.randint(1,1000),
         'luck':random.randint(1,1000),
         'happy':random.randint(1,1000),
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
         'creator':creator,                       # Айди бога, создавшего этого человека
         'variables':{'currentmoney':random.randint(0,1000000),
                      'acting':0,
                      'house':random.choice(houses),
                      'age':random.randint(18,100),
                      'atwork':0,
                      'student':random.randint(0,1),
                      'worker':random.randint(0,1),
                      'love':None,
                      'mood':random.randint(1,1000),
                      'friends':[],
                      'seer':None          # Внутренний голос: айди наблюдающего за человеком
                     },
         'func':{'preparetowork':0,
                 'tryfindwork':0,
                 'relax':0,
                 'gohome':0
                }
        }

def monthtodays(month):
  if month==1:
    return 31
  elif month==2:
    return 28
  elif month==3:
    return 31
  elif month==4:
    return 30
  elif month==5:
    return 31
  elif month==6:
    return 30
  elif month==7:
    return 31
  elif month==8:
    return 31
  elif month==9:
    return 30
  elif month==10:
    return 31
  elif month==11:
    return 30
  elif month==12:
    return 31
  
  
def life():
  t=threading.Timer(1, life)     # 1 секунда реальной жизни равна одной минуте в городе
  t.start()
  global year
  global month
  global day
  global hour
  global minute
  minute+=1
  if minute==60:
    minute=0
    hour+=1
  if hour==24:
    hour=0
    day+=1
  if day>monthtodays(month):
    day=1
    month+=1
  if month==13:
    month=1
    year+=1
  x=humans.find({})
  for ids in x:
    if ids['variables']['acting']==0:
      humanacts.actfind(ids, year, month, day, hour, minute)
  
def timewrite():
  global year
  global month
  global day
  global hour
  global minute
  t=threading.Timer(120, timewrite)
  t.start()
  citytime.update_one({}, {'$set':{'year':year}})
  citytime.update_one({}, {'$set':{'month':month}})
  citytime.update_one({}, {'$set':{'day':day}})
  citytime.update_one({}, {'$set':{'hour':hour}})
  citytime.update_one({}, {'$set':{'minute':minute}})



if True:
  timewrite()


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
