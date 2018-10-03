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

from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

client1=os.environ['database']
client=MongoClient(client1)
db=client.everlastingsummer
users=db.users


symbollist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

works={
           {'name':'concertready',
              'value':0,
              'lvl':1
             },
           {'name':'sortmedicaments',
              'value':0,
              'lvl':1
             },
           {'name':'checkpionerssleeping',
              'value':0,
              'lvl':1
             },
          
           {'name':'pickberrys',
            'value':0,
            'lvl':2
            },
           {'name':'bringfoodtokitchen',
            'value':0,
            'lvl':2
            },
           {'name':'helpinmedpunkt',
            'value':0,
            'lvl':2
            },
           {'name':'helpinkitchen',
            'value':0,
            'lvl':2
            },
          

           {'name':'cleanterritory',
              'value':0,
              'lvl':3
             },
           {'name':'washgenda',
              'value':0,
            'lvl':3
             }
       }

def lvlsort(x):
   finallist=[]
   if x==1:
      work=lvl1works
   elif x==2:
      work=lvl2works
   elif x==3:
      work=lvl3works
   for ids in work:
      if work[ids]['value']==0:
         finallist.append(work[ids]['name'])
   return finallist
           

@bot.message_handler(commands=['start'])
def start(m):
 if m.chat.id==m.from_user.id:
  x=users.find_one({'id':m.from_user.id})
  if x==None:
    users.insert_one(createuser(m.from_user.id, m.from_user.first_name, m.from_user.username))
    bot.send_message(m.chat.id,'Здраствуй, пионер! Меня зовут Ольга Дмитриевна, я буду твоей вожатой. Впереди тебя ждёт интересная жизнь в лагере "Совёнок"! '+
                     'А сейчас скажи нам, как тебя зовут (следующим сообщением).')
  else:
   if x['setgender']==0 and x['setname']==0:
    x=users.find_one({'id':m.from_user.id})
    if x['working']==1:
       bot.send_message(m.chat.id, 'Здраствуй, пионер! Вижу, ты занят. Молодец! Не буду отвлекать.')
    else:
       bot.send_message(m.chat.id, 'Здраствуй, пионер! Отдыхаешь? Могу найти для тебя найти занятие!')
  


@bot.message_handler(commands=['work'])
def work(m):
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
      if x['setgender']==0 and x['setname']==0:
        if x['working']==0:
          if x['waitforwork']==0:
           if x['relaxing']==0:
            users.update_one({'id':m.from_user.id},{'$set':{'waitforwork':1}})
            bot.send_message(m.chat.id, random.choice(worktexts), reply_to_message_id=m.message_id)
            t=threading.Timer(random.randint(60,120),givework, args=[m.from_user.id])
            t.start()
           else:
              bot.send_message(m.chat.id, 'Нельзя так часто работать! Хвалю, конечно, за трудолюбивость, но сначала отдохни.', reply_to_message_id=m.message_id)
           
          
def givework(id):
    x=users.find_one({'id':id})
    if x!=None:
       text=''
       if x['gender']=='male':
          gndr=''
       if x['gender']=='female':
          gndr='а'
       lvl1quests=lvlsort(1)
       lvl2quests=lvlsort(2)
       lvl3quests=lvlsort(3)
       sendto=types.ForceReply(selective=False)
       users.update_one({'id':id},{'$set':{'answering':1}})
       quest=None
       if x['OlgaDmitrievna_respect']>=75:
           text+='Так как ты у нас ответственный пионер, ['+x['pionername']+'](tg://user?id='+str(id)+'), у меня для тебя есть важное задание!\n'
           if len(lvl1quests)>0:
               quest=random.choice(lvl1quests)
               if quest=='concertready':
                  text+='Тебе нужно подготовить сцену для сегодняшнего выступления: принести декорации и аппаратуру, которые нужны выступающим пионерам, выровнять стулья. Приступишь?'
               elif quest=='sortmedicaments':
                  text+='Тебе нужно помочь медсестре с лекарствами. Не знаю точно, что там требуется, уточнишь у неё. Возьмёшься?'
               elif quest=='checkpionerssleeping':
                  text+='Уже вечер, и все пионеры должны в это время ложиться спать. Пройдись по лагерю и поторопи гуляющих. Готов'+gndr+'?'
               users.update_one({'id':id},{'$set':{'prepareto':quest}})
               bot.send_message(-1001351496983, text, reply_markup=sendto, parse_mode='markdown')
               users.update_one({'id':id},{'$set':{'answering':1}})
               t=threading.Timer(60, cancelquest, args=[id])
               t.start()
           else:
               text='Важных заданий на данный момент нет, ['+x['pionername']+'](tg://user?id='+str(id)+')... Но ничего, обычная работа почти всегда найдётся!\n'
               questt=[]
               if len(lvl2quests)>0:
                  questt.append(random.choice(lvl2quests))
               if len(lvl3quests)>0:
                  questt.append(random.choice(lvl3quests))
               if len(questt)>0:
                  quest=random.choice(questt)
                  if quest=='pickberrys':
                     text+='Собери-ка ягоды для вечернего торта! Ты готов, пионер?'
                  if quest=='bringfoodtokitchen':
                     text+='На кухне не хватает продуктов. Посети библиотеку, кружок кибернетиков и медпункт, там должны быть некоторые ингридиенты. Справишься?'
                  if quest=='washgenda':
                      if x['gender']=='female':
                          gndr='ла'
                      text+='Наш памятник на главной площади совсем запылился. Не мог'+gndr+' бы ты помыть его?'
                  if quest=='cleanterritory':
                      text+='Территория лагеря всегда должна быть в чистоте! Возьми веник и совок, и подмети здесь всё. Справишься?'
                  bot.send_message(-1001351496983, text, reply_markup=sendto, parse_mode='markdown')
                  users.update_one({'id':id},{'$set':{'prepareto':quest}})
                  users.update_one({'id':id},{'$set':{'answering':1}})
               else:
                   bot.send_message(-1001351496983, 'К сожалению, заданий для тебя сейчас нет, ['+x['pionername']+'](tg://user?id='+str(id)+'). Но за желание помочь лагерю хвалю!', reply_markup=sendto, parse_mode='markdown')
       elif x['OlgaDmitrievna_respect']>=40:
           text+='Нашла для тебя занятие, ['+x['pionername']+'](tg://user?id='+str(id)+')!\n'
           quest=random.choice(lvl2quests)
           if quest=='pickberrys':
              text+='Собери-ка ягоды для вечернего торта! Ты готов, пионер?'
           if quest=='bringfoodtokitchen':
              text+='На кухне не хватает продуктов. Посети библиотеку, кружок кибернетиков и медпункт, там должны быть некоторые ингридиенты. Справишься?'
           if quest=='helpinmedpunkt':
              text+='Медсестре нужна какая-то помощь. Точно не знаю, но пойди узнай у неё. Приступишь?'
           if quest=='helpinkitchen':
              if x['gender']=='female':
                  gndr='а'
              text+='На кухне не хватает людей! Было бы хорошо, если бы ты помог им с приготовлением. Готов'+gndr+'?'
           sendto=types.ForceReply(selective=False)
           users.update_one({'id':id},{'$set':{'prepareto':quest}})
           bot.send_message(-1001351496983, text, reply_markup=sendto, parse_mode='markdown')
           users.update_one({'id':id},{'$set':{'answering':1}})
           t=threading.Timer(60, cancelquest, args=[id])
           t.start()
       else:
           text+='Ответственные задания я тебе пока что доверить не могу, ['+x['pionername']+'](tg://user?id='+id+'). Чтобы вырастить из тебя образцового пионера, начнем с малого.\n'
           quest=random.choice(lvl3quests)
           if quest=='washgenda':
              if x['gender']=='female':
                 gndr='ла'
              text+='Наш памятник на главной площади совсем запылился. Не мог'+gndr+' бы ты помыть его?'
           if quest=='cleanterritory':
              text+='Территория лагеря всегда должна быть в чистоте! Возьми веник и совок, и подмети здесь всё. Справишься?'
           sendto=types.ForceReply(selective=False)
           users.update_one({'id':id},{'$set':{'prepareto':quest}})
           bot.send_message(-1001351496983, text, reply_markup=sendto, parse_mode='markdown')
           users.update_one({'id':id},{'$set':{'answering':1}})
           t=threading.Timer(60, cancelquest, args=[id])
           t.start()
           
           
def cancelquest(id):
    x=users.find_one({'id':id})
    if x!=None:
        if x['answering']==1:
            users.update_one({'id':id},{'$set':{'prepareto':None}})
            users.update_one({'id':id},{'$set':{'answering':0}})
            users.update_one({'id':id},{'$set':{'waitforwork':0}})
            bot.send_message(-1001351496983, '['+x['pionername']+'](tg://user?id='+str(id)+')! Почему не отвечаешь? Неприлично, знаешь ли. Ну, раз не хочешь, найду другого пионера для этой работы.',parse_mode='markdown')
            
            


worktexts=['Ну что, пионер, скучаешь? Ничего, сейчас найду для тебя подходящее занятие! Подожди немного.',
           'Бездельничаешь? Сейчас я это исправлю! Подожди пару минут, найду тебе занятие.']
  
@bot.message_handler()
def messag(m):
  print(str(m.chat.id))
  if m.from_user.id==m.chat.id:
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
        if x['setname']==1:
            nott=0
            for ids in m.text:
                if ids.lower() not in symbollist:
                    nott=1
            if nott==0:
                users.update_one({'id':m.from_user.id},{'$set':{'pionername':m.text}})
                users.update_one({'id':m.from_user.id},{'$set':{'setname':0}})
                bot.send_message(m.chat.id, 'Отлично! И еще одна просьба... Прости конечно, но это нужно для документа, в котором '+
                                 'хранится информация обо всех пионерах. Я, конечно, сама вижу, но это надо сделать твоей рукой. '+
                                 'Напиши вот тут свой пол (М или Д).')
            else:
                bot.send_message(m.chat.id, 'Нет-нет! Имя может содержать только буквы русского и английского алфавита!')
        else:
            if x['setgender']==1:
                  da=0
                  if m.text.lower()=='м':
                        users.update_one({'id':m.from_user.id},{'$set':{'setgender':0}})
                        users.update_one({'id':m.from_user.id},{'$set':{'gender':'male'}})
                        da=1
                  elif m.text.lower()=='д':
                        users.update_one({'id':m.from_user.id},{'$set':{'setgender':0}})
                        users.update_one({'id':m.from_user.id},{'$set':{'gender':'female'}})
                        da=1
                  if da==1:
                      bot.send_message(m.chat.id, 'Добро пожаловать в лагерь, '+x['pionername']+'! Заходи в '+
                                 '@(Ссылка на лагерь пока неизвестна, подождите немного), и знакомься с остальными пионерами!')
      
  else:
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
      if x['setgender']==0 and x['setname']==0:
        if m.reply_to_message!=None:
          if m.reply_to_message.from_user.id==636658457:
             if x['answering']==1:
               if m.text=='Хорошо, Ольга Дмитриевна!':
                 users.update_one({'id':m.from_user.id},{'$set':{'answering':0}})
                 users.update_one({'id':m.from_user.id},{'$set':{'working':1}})
                 users.update_one({'id':m.from_user.id},{'$set':{'waitforwork':0}})
                 dowork(m.from_user.id)
                 users.update_one({'id':m.from_user.id},{'$set':{'prepareto':None}})
                 bot.send_message(m.chat.id,'Молодец, пионер! Как закончишь - сообщи мне.',reply_to_message_id=m.message_id )
           
def dowork(id):
    x=users.find_one({'id':id})
    for ids in lvl1works:
        if lvl1works[ids]
     
    
     
    
         
    t=threading.Timer(300, endwork, args=[id])
    t.start()
    
    
def endwork(id):
    x=users.find_one({'id':id})
    users.update_one({'id':id},{'$set':{'working':0}})
    users.update_one({'id':id},{'$set':{'relaxing':1}})
    bot.send_message(-1001351496983, 'Отличная работа, ['+x['pionername']+'](tg://user?id='+str(id)+')! Теперь можешь отдохнуть.', parse_mode='markdown')
    t=threading.Timer(600,relax,args=[id])
    t.start()
    
def relax(id):
    users.update_one({'id':id},{'$set':{'relaxing':0}})
    
    
    
def createuser(id, name, username):
    return{'id':id,
           'name':name,
           'username':username,
           'pionername':None,
           'gender':None,
           'strenght':3,
           'agility':3,
           'intelligence':3,
           'prepareto':None,           
           'setname':1,
           'setgender':1,
           'waitforwork':0,
           'respect':50,
           'working':0,
           'relaxing':0,
           'answering':0,
           'OlgaDmitrievna_respect':50,
           'Slavya_respect':50,
           'Uliana_respect':50,
           'Alisa_respect':50,
           'Lena_respect':50,
           'Electronic_respect':50,
           'Miku_respect':50,
           'Zhenya_respect':50
           
          }
    
    
    
if True:
   print('7777')
   users.update_many({},{'$set':{'working':0}})
   users.update_many({},{'$set':{'waitforwork':0}})
   users.update_many({},{'$set':{'relaxing':0}})
   bot.polling(none_stop=True,timeout=600)

