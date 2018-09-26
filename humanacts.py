client1=os.environ['database']
client=MongoClient(client1)
db=client.worldseer
humans=db.humans
users=db.users
citytime=db.citytime


def actfind(human, year, month, day, hour, minute):
  if human['age']<=22:
    if hour>=22 or hour<=5:
      if human['athome']==0:
       if len(human['variables']['friends'])>0:
         if human['variables']['mood']>=500:
           if human['variables']['seer']!=None:
             if random.randint(1,100)<=50:
               askgod(human, 'callfriend', human['variables']['seer'])
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
    if hour>=6 and hour<=8:
      pass
  elif human['age']<=35:
    pass
  elif human['age']<=60:
    pass
  elif human['age']<=85:
    pass
  elif human['age']<=110:
    pass

  
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
