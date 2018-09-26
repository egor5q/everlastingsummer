def actfind(human, year, month, day, hour, minute):
  if human['age']<=22:
    if hour>=22:
      if human['athome']==0:
        gohome(human)
    elif hour<=5:
      if human['athome']==0:
        gohome(human)
    
  elif human['age']<=35:
    pass
  elif human['age']<=60:
    pass
  elif human['age']<=85:
    pass
  elif human['age']<=110:
    pass
