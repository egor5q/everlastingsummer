client1=os.environ['database']
client=MongoClient(client1)
db=client.worldseer
humans=db.humans
users=db.users
citytime=db.citytime


def actfind(human, year, month, day, hour, minute):
  if human['age']<=22:
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
          
  elif human['age']<=35:
    pass
  elif human['age']<=60:
    pass
  elif human['age']<=85:
    pass
  elif human['age']<=110:
    pass

def foundwork(human):
  x=((human['attentiveness']/60)+(human['diligence']/60))*(human['luck']/385)
  z=random.randint(1,100)
  if z<=x:
    foundedwork(human)
    humans.update_one({'id':human['id']},{'$inc':{'variables.mood':55}})
  else:
    humans.update_one({'id':human['id']},{'$inc':{'variables.mood':-14}})
    
  
def foundedwork(human):
  humans.update_one({'id':human['id']},{'$set':{'variables.worker':1}})
  
  
def tryfindwork(human):
  t=threading.Timer(180, actend, args=[human])
  t.start()
  t=threading.Timer(180, foundwork, args=[human])
  t.start()
  x=int(8/((human['happy']/550)*(human['diligence']/420)))
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
  t=threading.Timer(30, actend, args=[human])
  t.start()
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':1}})
  humans.update_one({'id':human['id']},{'$inc':{'variables.mood':10}})
    
    
  
def actend(human):
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':0}})
  
def tohome(human):
  humans.update_one({'id':human['id']},{'$set':{'variables.athome':1}})

def gohome(human):
  t=threading.Timer(60, actend, args=[human])
  t.start()
  f=threading.Timer(60, tohome, args=[human])
  f.start()
  humans.update_one({'id':human['id']},{'$set':{'variables.acting':1}})
  
  
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
