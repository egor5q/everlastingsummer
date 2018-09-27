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
humans=db.humans
users=db.users
citytime=db.citytime


def actfind(human, year, month, day, hour, minute):
  if human['variables']['age']<=22:
    if hour>=22 or hour<=5:
      if human['variables']['athome']==0:
       if len(human['variables']['friends'])>0:
         if human['variables']['mood']>=500:
           if human['variables']['seer']!=None:
             if random.randint(1,100)<=50:
               askgod(human, 'callfriend')
             else:
               if random.randint(1,100)<=20:
                  callfriend(human)
               else:
                gohome(human)
           else:
              gohome(human)
         else:
            gohome(human)
       else:
        gohome(human)          
      else:
        homework(human)
    elif hour>=6 and hour<=8:
      if human['variable']['student']==1 or human['variable']['worker']==1:
        if human['variables']['mood']>=150 and human['diligence']>=230:
          preparetowork(human)
        else:
          if random.randint(1,100)<=50:
            relax(human)
          else:
            preparetowork(human)
      else:
        tryfindwork(human)
    elif hour>=9 and hour<=16:
      if human['variables']['atwork']==0:
        if human['variable']['student']==1 or human['variable']['worker']==1:
          if human['variables']['mood']>=330 and human['diligence']>=340:
            gotowork(human)
          else:
            if random.randint(1,100)<=50:
              askgod(human, 'gotowork')
            else:
              if random.randint(1,100)<=50:
                gotowork(human)
              else:
                relax(human)
        else:
          x=random.randint(1,2)
          if x==1:
            tryfindwork(human)
          elif x==2:
            relax(human)
      else:
        dowork(human)
        
  elif human['age']<=35:
    pass
  elif human['age']<=60:
    pass
  elif human['age']<=85:
    pass
  elif human['age']<=110:
    pass

def dowork(human):
  if human['variables']['student']==1:
    t=threading.Timer(360, actend, args=[human])
    t.start()
    if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], human['name']+' учится! Закончит через 6 часов.')
    if human['diligence']>=735:
      mood=25
      if human['variables']['seer']!=None:
        bot.send_message(human['variables']['seer'], '"В принципе, на учёбе не так уж и плохо. От этого можно даже получать удовольствие!"'+
                         ' - мысли человека "'+human['name']+'".')
    else:
      mood=-15
      if human['variables']['seer']!=None:
        bot.send_message(human['variables']['seer'], '"Не люблю учебу... Скукота!"')
    humans.update_one({'id':human['id']},{'$inc':{'variables.mood':mood}})
  
  
def preparetowork(human):
  x=citytime.find_one({})
  x=x['day']
  humans.update_one({'id':human['id']},{'$set':{'func.preparetowork':1}})
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':1}})
  if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], human['name']+' готовится к новому дню.\n"Сегодня '+str(x)+'е число. Пора собираться!"')
  t=threading.Timer(50, actend, args=[human])
  t.start()
  
  
def foundwork(human):
  humans.update_one({'id':human['id']},{'$set':{'func.foundwork':1}})
  x=((human['attentiveness']/60)+(human['diligence']/60))*(human['luck']/385)
  z=random.randint(1,100)
  if z<=x:
    foundedwork(human)
    humans.update_one({'id':human['id']},{'$inc':{'variables.mood':55}})
    if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], '"Ура! Я нашел работу!"')
  else:
    if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'],'"Я не смог найти работу... Попробую в другой раз."')
    humans.update_one({'id':human['id']},{'$inc':{'variables.mood':-14}})
    
  
def foundedwork(human):
  humans.update_one({'id':human['id']},{'$set':{'variables.worker':1}})
  
  
def tryfindwork(human):
  if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'],'"Попробую найти работу..."')
  t=threading.Timer(180, actend, args=[human])
  t.start()
  t=threading.Timer(180, foundwork, args=[human])
  t.start()
  x=int(8/((human['happy']/550)*(human['diligence']/420)))
  humans.update_one({'id':human['id']},{'$set':{'func.tryfindwork':1}})
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':1}})
  humans.update_one({'id':human['id']},{'$inc':{'variables.mood':-x}})
  
  
def homework(human):
 if human['variables']['homeworkready']==0 and human['variable']['student']==1:
  if human['diligence']>=350 and human['variables']['mood']>=320:
    if random.randint(1,100)<=95:
      dohomework(human)           # Уроки
    else:
      relax(human)
  else:
    if random.randint(1,100)<=45:
      dohomework(human)
    else:
      relax(human)
 else:
  relax(human)
    
def relax(human):
  humans.update_one({'id':human['id']},{'$set':{'func.relax':1}})
  x=citytime.find_one({})
  hour=x['hours']
  if hour>=22 or hour<=4:
    if hour>=22:
      p=24-hour
      p=7+p
    elif hour<=4:
      p=7-hour
    t=threading.Timer(p, actend, args=[human])
    t.start()
    if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], '"Сегодня был тяжелый день... Пойду спать!"')
  else:
    if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], '"Отдохну-ка я..."')
    t=threading.Timer(30, actend, args=[human])
    t.start()
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':1}})
  humans.update_one({'id':human['id']},{'$inc':{'variables.mood':10}})
    
    
  
def actend(human):
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':0}})
  humans.update_one({'id':human['id']},{'$set':{'func.preparetowork':0}})
  humans.update_one({'id':human['id']},{'$set':{'func.tryfindwork':0}})
  humans.update_one({'id':human['id']},{'$set':{'func.relax':0}})
  humans.update_one({'id':human['id']},{'$set':{'func.gohome':0}})
  
def tohome(human):
  humans.update_one({'id':human['id']},{'$set':{'variables.athome':1}})

def gohome(human):
  if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], human['name']+'"Иду домой..."')
  t=threading.Timer(60, actend, args=[human])
  t.start()
  f=threading.Timer(60, tohome, args=[human])
  f.start()
  humans.update_one({'id':human['id']},{'$set':{'func.gohome':1}})
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':1}})
  
def askgod(human, question):
  if question=='callfriend':
    if human['variables']['seer']!=None:
      bot.send_message(human['variables']['seer'], '"Как же поступить... В прочем, неважно!"')
  
  
