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
import traceback
#import re


from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError

token = os.environ['TELEGRAM_TOKEN']
world = os.environ['worldtoken']
bot = telebot.TeleBot(token)
world = telebot.TeleBot(world)
alisa = telebot.TeleBot(os.environ['alisa'])
miku = telebot.TeleBot(os.environ['miku'])
lena = telebot.TeleBot(os.environ['lena'])
slavya = telebot.TeleBot(os.environ['slavya'])
uliana = telebot.TeleBot(os.environ['uliana'])
electronic = telebot.TeleBot(os.environ['electronic'])
zhenya = telebot.TeleBot(os.environ['zhenya'])
tolik = telebot.TeleBot(os.environ['tolik'])
shurik = telebot.TeleBot(os.environ['shurik'])
semen = telebot.TeleBot(os.environ['semen'])
pioneer = telebot.TeleBot(os.environ['pioneer'])

client1 = os.environ['database']
client = MongoClient(client1)
db = client.everlastingsummer
users = db.users
thunder = db.thunder
thunder_variables = db.thunder_variables
ban = db.ban

mainchat = -1001351496983
rpchats=[]


yestexts = ['хорошо, ольга дмитриевна!', 'хорошо!', 'я этим займусь!', 'я готов!', 'я готова!']
notexts = ['простите, но у меня уже появились дела.']

botadmins = [441399484]
el_admins = []#[574865060, 524034660]
al_admins = []#[512006137, 737959649]
ul_admins = [652585389]#[851513241]
mi_admins = []#[268486177]
le_admins = []#[60727377, 851513241]
sl_admins = []#[851513241]
od_admins = []#[629070350, 512006137, 850666493]
zh_admins = []#[390362465]
to_admins = []#[414374606]
sh_admins = []#[574865060]
se_admins = []#[851513241, 737959649]
pi_admins = []#[512006137]

ignorelist = []

rds = False

works = [
    {'name': 'concertready',
     'value': 0,
     'lvl': 1
     },
    {'name': 'sortmedicaments',
     'value': 0,
     'lvl': 2
     },
    {'name': 'checkpionerssleeping',
     'value': 0,
     'lvl': 1
     },

    {'name': 'pickberrys',
     'value': 0,
     'lvl': 2
     },
    {'name': 'bringfoodtokitchen',
     'value': 0,
     'lvl': 2
     },
    {'name': 'helpinmedpunkt',
     'value': 0,
     'lvl': 1
     },
    {'name': 'helpinkitchen',
     'value': 0,
     'lvl': 2
     },

    {'name': 'cleanterritory',
     'value': 0,
     'lvl': 3
     },
    {'name': 'washgenda',
     'value': 0,
     'lvl': 3
     }
]


def createban(id):
    return {
        'id': id
    }


if ban.find_one({'id': 617640951}) == None:
    ban.insert_one(createban(617640951))


@world.message_handler(commands=['do'])
def do(m):
    try:
        if m.from_user.id == 441399484:
            cmd = m.text.split('/do ')[1]
            try:
                eval(cmd)
                world.send_message(m.chat.id, 'Success')
            except:
                world.send_message(441399484, traceback.format_exc())
    except:
        pass


@bot.message_handler(commands=['ignore'])
def ignore(m):
    if m.from_user.id == 441399484:
        try:
            x = int(m.text.split(' ')[1])
            if x > 0:
                ignorelist.append(x)
                bot.send_message(m.chat.id, 'Теперь айди ' + str(x) + ' игнорится!')
        except:
            pass


@world.message_handler(commands=['switch'])
def do(m):
    if m.from_user.id == 441399484:
        global rds
        rds = not rds
        if rds == True:
            world.send_message(m.chat.id, 'now True')
        else:
            world.send_message(m.chat.id, 'now False')


def worktoquest(work):
    if work == 'concertready':
        return 'Подготовиться к вечернему концерту'
    if work == 'sortmedicaments':
        return 'Отсортировать лекарства в медпункте'
    if work == 'checkpionerssleeping':
        return 'На вечер - проследить за тем, чтобы в 10 часов все были в домиках'
    if work == 'pickberrys':
        return 'Собрать ягоды для торта'
    if work == 'bringfoodtokitchen':
        return 'Принести на кухню нужные ингридиенты'
    if work == 'helpinmedpunkt':
        return 'Последить за медпунктом, пока медсестры не будет'
    if work == 'helpinkitchen':
        return 'Помочь с приготовлением еды на кухне'
    if work == 'cleanterritory':
        return 'Подмести территорию лагеря'
    if work == 'washgenda':
        return 'Помыть памятник на главной площади'


def lvlsort(x):
    finallist = []
    for ids in works:
        if ids['lvl'] == x and ids['value'] == 0:
            finallist.append(ids['name'])
    return finallist



def stickhandler(m, pioner):
    if ban.find_one({'id': m.from_user.id}) == None:
        stats = None
        if pioner == uliana:
            stats = ulianastats
        if pioner == lena:
            stats = lenastats
        if pioner == tolik:
            stats = tolikstats
        if pioner == alisa:
            stats = alisastats
        if pioner == bot:
            stats = odstats
        if pioner == zhenya:
            stats = zhenyastats
        if pioner == shurik:
            stats = shurikstats
        if pioner == electronic:
            stats = electronicstats
        if pioner == slavya:
            stats = slavyastats
        if pioner == miku:
            stats = mikustats
        if pioner == pioneer:
            stats = pioneerstats
        if pioner == semen:
            stats = semenstats

        if stats['controller'] != None:
            controller = stats['controller']
            if m.from_user.id == controller['id']:
                if m.reply_to_message == None:
                    try:
                        bot.delete_message(m.chat.id, m.message_id)
                    except:
                        bot.send_message(441399484, traceback.format_exc())
                    pioner.send_sticker(m.chat.id, m.sticker.file_id)
                else:
                    try:
                        bot.delete_message(m.chat.id, m.message_id)
                    except:
                        bot.send_message(441399484, traceback.format_exc())
                    pioner.send_sticker(m.chat.id, m.sticker.file_id, reply_to_message_id=m.reply_to_message.message_id)
    

def msghandler(m, pioner):
    if ban.find_one({'id': m.from_user.id}) == None:
        stats = None
        if pioner == uliana:
            stats = ulianastats
        if pioner == lena:
            stats = lenastats
        if pioner == tolik:
            stats = tolikstats
        if pioner == alisa:
            stats = alisastats
        if pioner == bot:
            stats = odstats
        if pioner == zhenya:
            stats = zhenyastats
        if pioner == shurik:
            stats = shurikstats
        if pioner == electronic:
            stats = electronicstats
        if pioner == slavya:
            stats = slavyastats
        if pioner == miku:
            stats = mikustats
        if pioner == pioneer:
            stats = pioneerstats
        if pioner == semen:
            stats = semenstats

        if stats['controller'] != None:
            controller = stats['controller']
            if m.from_user.id == controller['id']:
              if m.text[0]!='/':
                if m.reply_to_message == None:
                    #if m.text.split(' ')[0] != '/pm' and m.text.split(' ')[0] != '/r':
                    try:
                        bot.delete_message(chat_id=m.chat.id, message_id=m.message_id)
                    except:
                        bot.send_message(441399484, traceback.format_exc())
                    msg = pioner.send_message(m.chat.id, m.text)
                        #for ids in ctrls:
                        #    if ids['controller'] != None and ids['bot'] != pioner:
                        #        if msg.chat.id == -1001351496983:
                        #            x = '(Общий чат)'
                        #        else:
                        #            x = '(ЛС)'
                        #        try:
                        #            ids['bot'].send_message(ids['controller']['id'],
                        #                                    x + '\n' + msg.from_user.first_name + ' (`' + str(
                        #                                        msg.from_user.id) + '`) (❓' + str(
                        #                                        msg.message_id) + '⏹):\n' + msg.text,
                        #                                    parse_mode='markdown')
                        #        except Exception as E:
                        #            bot.send_message(441399484, traceback.format_exc())
                    #elif m.text.split(' ')[0] == '/pm':
                    #    try:
                    #        text = m.text.split(' ')
                    #        t = ''
                    #        i = 0
                    #        for ids in text:
                    #            if i > 1:
                    #                t += ids + ' '
                    #            i += 1
                    #        pioner.send_message(int(m.text.split(' ')[1]), t)
                    #    except:
                    #        pioner.send_message(m.from_user.id, 'Что-то пошло не так. Возможны следующие варианты:\n' +
                    #                            '1. Неправильный формат отправки сообщения в ЛС юзера (пример: _/pm 441399484 Привет!_)\n' +
                    #                            '2. Юзер не написал этому пионеру/пионерке в ЛС.\nМожно реплайнуть на сообщение от меня, и я реплайну на оригинальное сообщение в чате!',
                    #                            parse_mode='markdown')

                else:
                    try:
                        #i = 0
                        #cid = None
                        #eid = None
                        #for ids in m.reply_to_message.text:
                        #    print(ids)
                        #    if ids == '❓':
                        #        cid = i + 1
                        #    if ids == '⏹':
                        #        eid = i
                        #    i += 1
                        #print('cid')
                        #print(cid)
                        #print('eid')
                        #print(eid)
                        #msgid = m.reply_to_message.text[cid:eid]
                        try:
                            bot.delete_message(m.chat.id, m.message_id)
                        except:
                            bot.send_message(441399484, traceback.format_exc())
                        pioner.send_message(m.chat.id, m.text, reply_to_message_id=m.reply_to_message.message_id)

                    except Exception as E:
                        bot.send_message(441399484, traceback.format_exc())
                        #pioner.send_message(m.from_user.id, 'Что-то пошло не так. Возможны следующие варианты:\n' +
                        #                    '1. Неправильный формат отправки сообщения в ЛС юзера (пример: _/pm 441399484 Привет!_)\n' +
                        #                    '2. Юзер не написал этому пионеру/пионерке в ЛС.\nМожно реплайнуть на сообщение от меня, и я реплайну на оригинальное сообщение в чате!',
                        #                    parse_mode='markdown')



            else:
                pass
                #if m.chat.id == -1001351496983:
                #    x = '(Общий чат)'
                #else:
                #    x = '(ЛС)'
                #if m.chat.id not in ignorelist:
                #    try:
                #        pioner.send_message(controller['id'], x + '\n' + m.from_user.first_name + ' (`' + str(
                #            m.from_user.id) + '`) (❓' + str(m.message_id) + '⏹):\n' + m.text, parse_mode='markdown')

                #    except Exception as E:
                #        bot.send_message(441399484, traceback.format_exc())


@bot.message_handler(commands=['pioner_left'])
def leftpioneeer(m):
    if m.from_user.id == 441399484:
        try:
            user = users.find_one({'id': int(m.text.split(' ')[1])})
            users.remove({'id': user['id']})
            bot.send_message(-1001351496983, user['name'] + ' покинул лагерь. Ждём тебя в следующем году!')
        except:
            bot.send_message(441399484, traceback.format_exc())


@bot.message_handler(commands=['allinfo'])
def allinfoaboutp(m):
    try:
        x = users.find({})
        text = ''
        text2 = ''
        text3 = ''
        for ids in x:
            if len(text) <= 1000:
                try:
                    text += ids['pionername'] + ' ' + '(' + ids['name'] + ')' + ' `' + str(ids['id']) + '`\n'
                except:
                    text += '(' + ids['name'] + ')' + ' `' + str(ids['id']) + '`\n'
            elif len(text2) <= 1000:
                try:
                    text2 += ids['pionername'] + ' ' + '(' + ids['name'] + ')' + ' `' + str(ids['id']) + '`\n'
                except:
                    text2 += '(' + ids['name'] + ')' + ' `' + str(ids['id']) + '`\n'
        bot.send_message(441399484, text, parse_mode='markdown')
        if text2 != '':
            bot.send_message(441399484, text2, parse_mode='markdown')
    except:
        bot.send_message(441399484, traceback.format_exc())


@bot.message_handler(commands=['start'])
def start(m):
    if m.chat.id == m.from_user.id and ban.find_one({'id': m.from_user.id}) == None:
        x = users.find_one({'id': m.from_user.id})
        if x == None:
            users.insert_one(createuser(m.from_user.id, m.from_user.first_name, m.from_user.username))
            bot.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            bot.send_message(m.chat.id,
                             'Здраствуй, пионер! Меня зовут Ольга Дмитриевна, я буду твоей вожатой. Впереди тебя ждёт интересная жизнь в лагере "Совёнок"! ' +
                             'А сейчас скажи нам, как тебя зовут (следующим сообщением).')
        else:
            if x['setgender'] == 0 and x['setname'] == 0:
                x = users.find_one({'id': m.from_user.id})
                bot.send_chat_action(m.chat.id, 'typing')
                time.sleep(4)
                if x['working'] == 1:
                    bot.send_message(m.chat.id, 'Здраствуй, пионер! Вижу, ты занят. Молодец! Не буду отвлекать.')
                else:
                    bot.send_message(m.chat.id, 'Здраствуй, пионер! Отдыхаешь? Могу найти для тебя занятие!')


@bot.message_handler(commands=['pioner'])
def pinfo(m):
    if m.from_user.id == 441399484:
        try:
            x = users.find_one({'id': m.reply_to_message.from_user.id})
            if x != None:
                text = ''
                for ids in x:
                    text += ids + ': ' + str(x[ids]) + '\n'
                bot.send_message(441399484, text)
        except:
            bot.send_message(441399484, traceback.format_exc())


@bot.message_handler(commands=['work'])
def work(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        global rds
        x = users.find_one({'id': m.from_user.id})
        if x != None and rds == True:
            if x['setgender'] == 0 and x['setname'] == 0:
                if x['working'] == 0:
                    if x['waitforwork'] == 0:
                        if x['relaxing'] == 0:
                            users.update_one({'id': m.from_user.id}, {'$set': {'waitforwork': 1}})
                            bot.send_chat_action(m.chat.id, 'typing')
                            time.sleep(4)
                            bot.send_message(m.chat.id, random.choice(worktexts), reply_to_message_id=m.message_id)
                            t = threading.Timer(random.randint(60, 120), givework, args=[m.from_user.id])
                            t.start()
                        else:
                            bot.send_chat_action(m.chat.id, 'typing')
                            time.sleep(4)
                            bot.send_message(m.chat.id,
                                             'Нельзя так часто работать! Хвалю, конечно, за трудолюбивость, но сначала отдохни.',
                                             reply_to_message_id=m.message_id)


def givework(id):
    nosend = 0
    x = users.find_one({'id': id})
    if x != None:
        try:
            text = ''
            if x['gender'] == 'male':
                gndr = ''
            if x['gender'] == 'female':
                gndr = 'а'
            quests = lvlsort(1)
            sendto = types.ForceReply(selective=False)

            quest = None
            bot.send_chat_action(id, 'typing')
            time.sleep(4)
            if x['OlgaDmitrievna_respect'] >= 75:
                lvl1quests = lvlsort(1)
                text += 'Так как ты у нас ответственный пионер, [' + x['pionername'] + '](tg://user?id=' + str(
                    id) + '), у меня для тебя есть важное задание!\n'
                if len(lvl1quests) > 0:
                    quest = random.choice(lvl1quests)
                    users.update_one({'id': id}, {'$set': {'prepareto': quest}})
                    print('Юзер готовится к квесту: ' + quest)
                    users.update_one({'id': id}, {'$set': {'answering': 1}})
                    t = threading.Timer(60, cancelquest, args=[id])
                    t.start()
                else:
                    text = 'Важных заданий на данный момент нет, [' + x['pionername'] + '](tg://user?id=' + str(
                        id) + ')... Но ничего, обычная работа почти всегда найдётся!\n'
                    questt = []
                    quest2 = lvlsort(2)
                    quest3 = lvlsort(3)
                    for ids in quest2:
                        questt.append(ids)
                    for ids in quest3:
                        questt.append(ids)
                    if len(questt) > 0:
                        quest = random.choice(questt)
                        print('Юзер готовится к квесту: ' + quest)
                        users.update_one({'id': id}, {'$set': {'prepareto': quest}})
                        users.update_one({'id': id}, {'$set': {'answering': 1}})
                    else:
                        nosend = 1
                        bot.send_message(-1001351496983, 'К сожалению, заданий для тебя сейчас нет, [' + x[
                            'pionername'] + '](tg://user?id=' + str(id) + '). Но за желание помочь лагерю хвалю!',
                                         parse_mode='markdown')
                        users.update_one({'id': id}, {'$set': {'waitforwork': 0}})
            elif x['OlgaDmitrievna_respect'] >= 40:
                text += 'Нашла для тебя занятие, [' + x['pionername'] + '](tg://user?id=' + str(id) + ')!\n'
                lvl2quests = lvlsort(2)
                if len(lvl2quests) > 0:
                    quest = random.choice(lvl2quests)
                    sendto = types.ForceReply(selective=False)
                    users.update_one({'id': id}, {'$set': {'prepareto': quest}})
                    users.update_one({'id': id}, {'$set': {'answering': 1}})
                    print('Юзер готовится к квесту: ' + quest)
                    t = threading.Timer(60, cancelquest, args=[id])
                    t.start()
                else:
                    lvl3quests = lvlsort(3)
                    if len(lvl3quests) > 0:
                        quest = random.choice(lvl3quests)
                        sendto = types.ForceReply(selective=False)
                        print('Юзер готовится к квесту: ' + quest)
                        users.update_one({'id': id}, {'$set': {'prepareto': quest}})
                        users.update_one({'id': id}, {'$set': {'answering': 1}})
                        t = threading.Timer(60, cancelquest, args=[id])
                        t.start()
                    else:
                        nosend = 1
                        bot.send_message(-1001351496983, 'К сожалению, заданий для тебя сейчас нет, [' + x[
                            'pionername'] + '](tg://user?id=' + str(id) + '). Но за желание помочь лагерю хвалю!',
                                         parse_mode='markdown')
                        users.update_one({'id': id}, {'$set': {'waitforwork': 0}})

            else:
                text += 'Ответственные задания я тебе пока что доверить не могу, [' + x[
                    'pionername'] + '](tg://user?id=' + str(
                    id) + '). Чтобы вырастить из тебя образцового пионера, начнем с малого.\n'
                lvl3quests = lvlsort(3)
                if len(lvl3quests) > 0:
                    quest = random.choice(lvl3quests)
                    sendto = types.ForceReply(selective=False)
                    users.update_one({'id': id}, {'$set': {'prepareto': quest}})
                    print('Юзер готовится к квесту: ' + quest)
                    users.update_one({'id': id}, {'$set': {'answering': 1}})
                    t = threading.Timer(60, cancelquest, args=[id])
                    t.start()
                else:
                    nosend = 1
                    bot.send_message(-1001351496983, 'К сожалению, заданий для тебя сейчас нет, [' + x[
                        'pionername'] + '](tg://user?id=' + str(id) + '). Но за желание помочь лагерю хвалю!',
                                     parse_mode='markdown')
            if quest == 'pickberrys':
                text += 'Собери-ка ягоды для вечернего торта! Ты готов, пионер?'
            if quest == 'bringfoodtokitchen':
                text += 'На кухне не хватает продуктов. Посети библиотеку, кружок кибернетиков и медпункт, там должны быть некоторые ингридиенты. Справишься?'
            if quest == 'washgenda':
                if x['gender'] == 'female':
                    gndr = 'ла'
                text += 'Наш памятник на главной площади совсем запылился. Не мог' + gndr + ' бы ты помыть его?'
            if quest == 'cleanterritory':
                text += 'Территория лагеря всегда должна быть в чистоте! Возьми веник и совок, и подмети здесь всё. Справишься?'
            if quest == 'concertready':
                text += 'Тебе нужно подготовить сцену для сегодняшнего выступления: принести декорации и аппаратуру, которые нужны выступающим пионерам, выровнять стулья. Приступишь?'
            if quest == 'sortmedicaments':
                text += 'Тебе нужно помочь медсестре: отсортировать привезённые недавно лекарства по ящикам и полкам. Возьмёшься?'
            if quest == 'checkpionerssleeping':
                text += 'Уже вечер, и все пионеры должны в это время ложиться спать. Пройдись по лагерю и поторопи гуляющих. Готов' + gndr + '?'
            if quest == 'helpinmedpunkt':
                text += 'Медсестре нужна твоя помощь: ей срочно нужно в райцентр. Посидишь в медпункте за неё?'
            if quest == 'helpinkitchen':
                gndr2 = ''
                if x['gender'] == 'female':
                    gndr = 'а'
                    gndr2 = 'ла'
                text += 'На кухне не хватает людей! Было бы хорошо, если бы ты помог' + gndr2 + ' им с приготовлением. Готов' + gndr + '?'
            if nosend == 0:
                users.update_one({'id': id}, {'$set': {'answering': 1}})
                bot.send_message(-1001351496983, text, parse_mode='markdown')
        except:
            bot.send_message(441399484, traceback.format_exc())


def cancelquest(id):
    x = users.find_one({'id': id})
    if x != None:
        if x['answering'] == 1:
            users.update_one({'id': id}, {'$set': {'prepareto': None}})
            users.update_one({'id': id}, {'$set': {'answering': 0}})
            users.update_one({'id': id}, {'$set': {'waitforwork': 0}})
            bot.send_message(-1001351496983, '[' + x['pionername'] + '](tg://user?id=' + str(
                id) + ')! Почему не отвечаешь? Неприлично, знаешь ли. Ну, раз не хочешь, найду другого пионера для этой работы.',
                             parse_mode='markdown')
            users.update_one({'id': id}, {'$inc': {'OlgaDmitrievna_respect': -4}})


worktexts = ['Ну что, пионер, скучаешь? Ничего, сейчас найду для тебя подходящее занятие! Подожди немного.',
             'Бездельничаешь? Сейчас я это исправлю! Подожди пару минут, найду тебе занятие.',
             'Здравствуй, пионер! Сейчас найду, чем тебя занять.']


@bot.message_handler(commands=['cards'])
def gamestestdsdfsdgd(m):
    if rds == True:
        if electronicstats['waitingplayers'] != 1:
            eveninggames()


####################################### OLGA ##############################################
@bot.message_handler(commands=['control'])
def odcontrol(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        if m.from_user.id in botadmins or m.from_user.id in od_admins:
            if odstats['controller'] == None:
                odstats['controller'] = {'id': m.from_user.id,
                                         'name': m.from_user.first_name}
                bot.send_message(m.from_user.id,
                                 'Здравствуй, пионер. Быть вожатым - большая ответственность! Не опозорь меня!')
            else:
                bot.send_message(m.from_user.id, 'Мной уже управляет ' + odstats['controller']['name'] + '!')


@bot.message_handler(commands=['stopcontrol'])
def odstopcontrol(m):
    if odstats['controller'] != None:
        if odstats['controller']['id'] == m.from_user.id:
            odstats['controller'] = None
            bot.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@bot.message_handler(content_types=['sticker'])
def stickercatchod(m):
    if m.from_user.id == 441399484:
        bot.send_message(441399484, m.sticker.file_id)
    stickhandler(m, bot)


@bot.message_handler()
def messag(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        if m.from_user.id == m.chat.id:
            x = users.find_one({'id': m.from_user.id})
            if x != None:
                if x['setname'] == 1:
                    correct_name = re.search('^[a-z,A-Z,а-я,А-Я]*$', m.text)
                    if correct_name:
                        users.update_one({'id': m.from_user.id}, {'$set': {'pionername': m.text}})
                        users.update_one({'id': m.from_user.id}, {'$set': {'setname': 0}})
                        bot.send_message(m.chat.id,
                                         'Отлично! И еще одна просьба... Прости конечно, но это нужно для документа, в котором ' +
                                         'хранится информация обо всех пионерах. Я, конечно, сама вижу, но это надо сделать твоей рукой. ' +
                                         'Напиши вот тут свой пол (М или Д).')
                    else:
                        bot.send_message(m.chat.id,
                                         'Нет-нет! Имя может содержать только буквы русского и английского алфавита!')
                else:
                    if x['setgender'] == 1:
                        da = 0
                        if m.text.lower() == 'м':
                            users.update_one({'id': m.from_user.id}, {'$set': {'setgender': 0}})
                            users.update_one({'id': m.from_user.id}, {'$set': {'gender': 'male'}})
                            da = 1
                        elif m.text.lower() == 'д':
                            users.update_one({'id': m.from_user.id}, {'$set': {'setgender': 0}})
                            users.update_one({'id': m.from_user.id}, {'$set': {'gender': 'female'}})
                            da = 1
                        if da == 1:
                            bot.send_message(m.chat.id,
                                             'Добро пожаловать в лагерь, ' + x['pionername'] + '! Заходи в ' +
                                             '@everlastingsummerchat, и знакомься с остальными пионерами!')

        else:
            x = users.find_one({'id': m.from_user.id})
            if x != None:
                if x['setgender'] == 0 and x['setname'] == 0:
                    if m.reply_to_message != None:
                        if m.reply_to_message.from_user.id == 636658457:
                            if x['answering'] == 1:
                                if m.text.lower() in yestexts:
                                    users.update_one({'id': m.from_user.id}, {'$set': {'answering': 0}})
                                    users.update_one({'id': m.from_user.id}, {'$set': {'working': 1}})
                                    users.update_one({'id': m.from_user.id}, {'$set': {'waitforwork': 0}})
                                    dowork(m.from_user.id)
                                    users.update_one({'id': m.from_user.id}, {'$set': {'prepareto': None}})
                                    bot.send_message(m.chat.id, 'Молодец, пионер! Как закончишь - сообщи мне.',
                                                     reply_to_message_id=m.message_id)
                    lineykatexts = ['я здесь', 'я тута', 'я пришёл', 'я пришла', 'я пришёл!', 'я пришла!', 'я здесь!',
                                    'я здесь', 'я пришел', 'я пришел!']
                    if odstats['waitforlineyka'] == 1:
                        yes = 0
                        for ids in lineykatexts:
                            if ids in m.text.lower():
                                yes = 1
                        if yes == 1:
                            if x['gender'] == 'male':
                                g = 'шёл'
                            else:
                                g = 'шла'
                            odstats['lineyka'].append('[' + x['pionername'] + '](tg://user?id=' + str(id) + ')')
                            bot.send_message(m.chat.id, 'А вот и [' + x['pionername'] + '](tg://user?id=' + str(
                                id) + ') при' + g + ' на линейку!')

        msghandler(m, bot)


def reloadquest(index):
    works[index]['value'] = 0
    print('Квест ' + works[index]['name'] + ' обновлён!')


def dowork(id):
    x = users.find_one({'id': id})
    i = 0
    index = None
    for ids in works:
        if x['prepareto'] == ids['name']:
            work = ids
            index = i
        i += 1
    if index != None:
        works[index]['value'] = 1
        hour = gettime('h')
        minute = gettime('m')
        z = None
        if works[index]['name'] == 'sortmedicaments':
            z = random.randint(3600, 7200)
        if works[index]['name'] == 'pickberrys':
            z = random.randint(7200, 9200)
        if works[index]['name'] == 'bringfoodtokitchen':
            z = random.randint(2200, 3600)
        if works[index]['name'] == 'helpmedpunkt':
            z = random.randint(7200, 10200)
        if works[index]['name'] == 'cleanterritory' or works[index]['name'] == 'washgenda':
            z = random.randint(900, 2700)
        if z != None:
            t = threading.Timer(z, reloadquest, args=[index])
            t.start()
        t = threading.Timer(300, endwork, args=[id, works[index]['name']])
        t.start()


def endwork(id, work):
    t = threading.Timer(180, relax, args=[id])
    t.start()
    x = users.find_one({'id': id})
    users.update_one({'id': id}, {'$set': {'working': 0}})
    users.update_one({'id': id}, {'$set': {'relaxing': 1}})
    srtenght = 0
    agility = 0
    intelligence = 0
    if x['gender'] == 'female':
        gndr = 'а'
    else:
        gndr = ''
    text = 'Ты хорошо поработал' + gndr + '! Улучшенные характеристики:\n'
    if work == 'sortmedicaments':
        agility = random.randint(0, 2)
        strenght = random.randint(1, 100)
        if strenght <= 15:
            strenght = 1
        else:
            strenght = 0
        intelligence = random.randint(1, 100)
        if intelligence <= 10:
            intelligence = 1
        else:
            intelligence = 0
    if work == 'pickberrys':
        strenght = random.randint(0, 2)
        agility = random.randint(1, 100)
        if agility <= 50:
            agility = random.randint(0, 2)
        else:
            agility = 0
    if work == 'bringfoodtokitchen':
        strenght = random.randint(1, 2)
        agility = random.randint(1, 100)
        if agility <= 30:
            agility = random.randint(1, 2)
        else:
            agility = 0
    if work == 'helpmedpunkt':
        intelligence = random.randint(2, 3)
        strenght = random.randint(1, 100)
        if strenght <= 35:
            strenght = random.randint(1, 2)
        else:
            strenght = 0
        agility = random.randint(1, 100)
        if agility <= 5:
            agility = 1
        else:
            agility = 0
    if work == 'cleanterritory' or work == 'washgenda':
        strenght = random.randint(0, 2)
        agility = random.randint(0, 1)
    if work == 'checkpionerssleeping':
        agility = random.randint(1, 2)
        intelligence = random.randint(1, 100)
        if intelligence <= 40:
            intelligence = random.randint(0, 2)
        else:
            intelligence = 0
    if work == 'concertready' or work == 'checkpionerssleeping' or work == 'helpinmedpunkt':
        agility = 3
        intelligence = 4
        strenght = 3
    if work == 'helpinkitchen':
        agility = random.randint(1, 2)
        intelligence = 1
        strenght = random.randint(0, 1)
    if agility > 0:
        text += '*Ловкость*\n'
    if strenght > 0:
        text += '*Сила*\n'
    if intelligence > 0:
        text += '*Интеллект*\n'
    if text == 'Ты хорошо поработал' + gndr + '! Улучшенные характеристики:\n':
        text = 'Физических улучшений не заметно, но ты заслужил' + gndr + ' уважение вожатой!'
    users.update_one({'id': id}, {'$inc': {'strenght': strenght}})
    users.update_one({'id': id}, {'$inc': {'agility': agility}})
    users.update_one({'id': id}, {'$inc': {'intelligence': intelligence}})
    bot.send_message(-1001351496983, 'Отличная работа, [' + x['pionername'] + '](tg://user?id=' + str(
        id) + ')! Теперь можешь отдохнуть.', parse_mode='markdown')
    users.update_one({'id': id}, {'$inc': {'OlgaDmitrievna_respect': 1}})
    try:
        world.send_message(id, text, parse_mode='markdown')
    except:
        world.send_message(-1001351496983,
                           '[' + x['pionername'] + '](tg://user?id=' + str(id) + ')' + random.choice(worldtexts) + text,
                           parse_mode='markdown')


worldtexts = [
    ', чтобы знать, что происходит в лагере (в том числе и с вами), советую отписаться мне в личку. Можете считать меня своим внутренним голосом, потому что забивать себе голову тем, кто я на самом деле, не имеет смысла... Но а теперь к делу.\n\n',
    ', отпишись, пожалуйста, мне в личку. Ведь правильнее будет, если твоя личная информация будет оставаться при тебе, а не оглашаться на весь лагерь. Ладно, ближе к делу...\n\n']


def relax(id):
    users.update_one({'id': id}, {'$set': {'relaxing': 0}})


def createuser(id, name, username):
    return {'id': id,
            'name': name,
            'username': username,
            'pionername': None,
            'gender': None,
            'popularity': 1,
            'strenght': 3,
            'agility': 3,
            'intelligence': 3,
            'prepareto': None,
            'setname': 1,
            'setgender': 1,
            'waitforwork': 0,
            'respect': 50,
            'working': 0,
            'relaxing': 0,
            'answering': 0,
            'busy': [],
            'OlgaDmitrievna_respect': 50,
            'Slavya_respect': 50,
            'Uliana_respect': 50,
            'Alisa_respect': 50,
            'Lena_respect': 50,
            'Electronic_respect': 50,
            'Miku_respect': 50,
            'Zhenya_respect': 50,
            'helping': 0

            }


def gettime(t):
    x = time.ctime()
    x = x.split(" ")
    for ids in x:
        for idss in ids:
            if idss == ':':
                tru = ids
    x = tru
    x = x.split(":")
    minute = int(x[1])
    hour = int(x[0]) + 3
    if t == 'h':
        return hour
    elif t == 'm':
        return minute


def checktime():
    t = threading.Timer(60, checktime)
    t.start()
    hour = gettime('h')
    minute = gettime('m')
    if hour == 17 and minute == 0:
        x = findindex('concertready')
        works[x]['value'] = 0
    if hour == 21 and minute == 30:
        x = findindex('checkpionerssleeping')
        works[x]['value'] = 0
    if (hour == 8 and minute == 10) or (hour == 13 and minute == 0) or (hour == 20 and minute == 30):
        x = findindex('helpinkitchen')
        works[x]['value'] = 0
    if (hour == 19 and minute == 0):
        cardplayers = []
        eveninggames()
    if (hour == 7 and minute == 0):
        odstats['waitforlineyka'] = 1
        bot.send_chat_action(-1001351496983, 'typing')
        time.sleep(3)
        bot.send_message(-1001351496983, 'Доброе утро, пионеры! В 7:30 жду всех на линейке!')
    if (hour == 7 and minute == 30):
        odstats['waitforlineyka'] = 0
        bot.send_chat_action(-1001351496983, 'typing')
        time.sleep(3)
        bot.send_message(-1001351496983, 'Здраствуйте, пионеры! Сейчас проведём перекличку...')
        bot.send_chat_action(-1001351496983, 'typing')
        time.sleep(4)
        text = ''
        for ids in odstats['lineyka']:
            text += ids + '\n'
        bot.send_message(-1001351496983, text + '\nВот все, кто сегодня пришёл. Молодцы, пионеры! Так держать!' + \
                         'Сейчас расскажу о планах на день.', parse_mode='markdown')


def eveninggames():
    global rds
    if rds == True:
        egames = ['cards']  # ,'ropepulling']
        x = random.choice(egames)
        if x == 'cards':
            electronicstats['waitingplayers'] = 1
            leader = 'electronic'
            bot.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(3.5, sendmes, args=[bot,
                                                    'Уже 7 вечера, а это значит, что пора начинать наши вечерние игры! На сегодня ' + \
                                                    'у нас по плану придуманная Электроником карточная игра. [Электроник](https://t.me/ES_ElectronicBot), ' + \
                                                    'дальше расскажешь ты.', 'markdown'])
            t.start()
            time.sleep(4.5)
            electronic.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(2, sendmes, args=[electronic, 'Есть, Ольга Дмитриевна!', None])
            t.start()
            t = threading.Timer(2.1, sendstick, args=[electronic, 'CAADAgAD1QADgi0zDyFh2eUTYDzzAg'])
            t.start()
            time.sleep(4)
            electronic.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(10, sendmes, args=[electronic,
                                                   'Итак. Правила игры просты: надо выиграть, собрав на руке более сильную ' + \
                                                   'комбинацию, чем у соперника. Процесс игры заключается в том, что соперники поочереди ' + \
                                                   'забирают друг у друга карты. Делается это так: в свой ход вы выбираете одну из карт соперника, ' + \
                                                   'а он после этого может поменять любые 2 карты в своей руке местами. Вы эту перестановку ' + \
                                                   'видите, и после его действия можете изменить свой выбор. А можете не менять. ' + \
                                                   'Так повторяется 3 раза, и вы забираете последнюю карту, которую выберите. Затем ' + \
                                                   'такой же ход повторяется со стороны соперника. Всего каждый участник делает 3 хода, ' + \
                                                   'и после этого оба игрока вскрываются...', None])
            t.start()
            time.sleep(4)
            electronic.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            electronic.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            electronic.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(5, sendmes,
                                args=[electronic, 'Что смешного? Ладно, неважно. Все поняли правила? Отлично! Для ' + \
                                      'регистрации в турнире нужно подойти ко мне, и сказать: "`Хочу принять участие в турнире!`". ' + \
                                      'Регистрация заканчивается через 20 минут!', 'markdown'])
            t.start()
            t = threading.Timer(300, starttournier, args=['cards'])
            t.start()

        elif x == 'football':
            leader = 'uliana'
            bot.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(3.5, sendmes, args=[bot,
                                                    'Уже 7 вечера, а это значит, что пора начинать наши вечерние игры! На сегодня ' + \
                                                    'у нас по плану футбол! [Ульяна](https://t.me/ES_UlianaBot), ' + \
                                                    'расскажет вам про правила проведения турнира.', 'markdown'])
            t.start()
            time.sleep(4.5)
            uliana.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(2, sendmes, args=[uliana, 'Так точно, Ольга Дмитриевна!', None])
            t.start()
            t = threading.Timer(2.1, sendstick, args=[uliana, 'CAADAgADKQADgi0zD_inNy0pZyh0Ag'])
            t.start()
            time.sleep(4)
            uliana.send_chat_action(-1001351496983, 'typing')
            t = threading.Timer(5, sendmes, args=[uliana, 'Правила просты - не жульничать! Для записи на турнир ' + \
                                                  'подойдите ко мне и скажите "`Хочу участвовать!`". Вроде бы всё... Жду всех!',
                                                  'markdown'])
            t.start()
        elif x == 'ropepulling':
            leader = 'alisa'


setka = []


def starttournier(game):
    try:
        if game == 'cards':
            global cardplayers
            global setka
            newplayers = ['miku', 'slavya', 'zhenya', 'alisa', 'lena', 'uliana']
            specialrules = 0
            i = 0
            for ids in cardplayers:
                i += 1
            if i % 2 == 0:
                if i >= 10:
                    prm = 16
                elif i > 0:
                    prm = 8
                else:
                    prm = 0
            else:
                if i == 1:
                    prm = 4
                elif i == 3 or i == 5 or i == 7:
                    prm = 8
                elif i == 9:
                    prm = 12
                    specialrules = 1
            g = 0
            if prm > 0:
                while g < (prm - i):
                    randomplayer = random.choice(newplayers)
                    cardplayers.append(randomplayer)
                    newplayers.remove(randomplayer)
                    g += 1
                text = ''
                i = 0
                h = len(cardplayers)
                while i < (h / 2):
                    player1 = random.choice(cardplayers)
                    cardplayers.remove(player1)
                    player2 = random.choice(cardplayers)
                    cardplayers.remove(player2)
                    setka.append([player1, player2])
                    i += 1
                for ids in setka:
                    text += '\n\n'
                    vs = ' VS '
                    for idss in ids:
                        try:
                            int(idss)
                            x = users.find_one({'id': idss})
                            text += '[' + x['pionername'] + '](tg://user?id=' + str(x['id']) + ')' + vs
                        except:
                            text += nametopioner(idss) + vs
                        vs = ''
                electronic.send_chat_action(-1001351496983, 'typing')
                time.sleep(5)
                electronic.send_message(-1001351496983,
                                        'Ну что, все в сборе? Тогда вот вам турнирная сетка на первый этап:\n' + text,
                                        parse_mode='markdown')
                time.sleep(1.5)
                electronic.send_chat_action(-1001351496983, 'typing')
                time.sleep(3)
                electronic.send_message(-1001351496983,
                                        'А теперь прошу к столам! Каждый садится со своим соперником. Через 2 минуты начинается ' +
                                        'первый этап!')
                electronicstats['cardsturn'] = 1
                t = threading.Timer(120, cards_nextturn)
                t.start()
                for ids in setka:
                    i = 0
                    for idss in ids:
                        try:
                            int(idss)
                            i += 1
                        except:
                            if i == 0:
                                index = 1
                            elif i == 1:
                                index = 0
                            try:
                                int(ids[index])
                                talkwithplayer(ids[index], idss)
                            except:
                                pass
            else:
                electronic.send_message(-1001351496983,
                                        'К сожалению, игроков для турнира сегодня не набралось. Ну ничего, в следующий раз попробуем!')
    except:
        setka = []
        cardplayers = []
        electronicstats['waitingplayers'] = 0
        electronicstats['playingcards'] = 0
        electronicstats['cardsturn'] = 0
        electronic.send_message(-1001351496983, 'Непредвиденные обстоятельства! Турнир придётся отменить!')


def cards_nextturn():
    try:
        global setka
        global cardplayers
        for ab in setka:
            cardplayers.append(ab[0])
            cardplayers.append(ab[1])
        if len(cardplayers) > 0:
            print(setka)
            print(cardplayers)
            for ids in setka:
                i = -1
                print(ids)
                for idss in ids:
                    print(idss)
                    i += 1
                    if i < 2:
                        try:
                            print('try1')
                            int(ids[0])
                            if i == 0:
                                index = 1
                            else:
                                index = 0
                            try:
                                print('try2')
                                int(ids[index])
                                player1 = users.find_one({'id': ids[0]})
                                player2 = users.find_one({'id': ids[1]})
                                r = player1['intelligence'] - player2['intelligence']
                                r = r / 2
                                x = random.randint(1, 100)
                                if x <= (50 + r):
                                    cardplayers.remove(player2['id'])
                                else:
                                    cardplayers.remove(player1['id'])
                                i = 10
                                print('try2complete')

                            except:
                                coef = 0
                                user = users.find_one({'id': ids[1]})
                                if user != None:
                                    coef += user['intelligence']
                                if ids[index] == 'miku':
                                    intelligence = mikustats['intelligence']
                                if ids[index] == 'alisa':
                                    intelligence = alisastats['intelligence']
                                if ids[index] == 'lena':
                                    intelligence = lenastats['intelligence']
                                if ids[index] == 'slavya':
                                    intelligence = slavyastats['intelligence']
                                if ids[index] == 'zhenya':
                                    intelligence = zhenyastats['intelligence']
                                if ids[index] == 'uliana':
                                    intelligence = ulianastats['intelligence']
                                if intelligence == 1:
                                    x = 80 + coef
                                if intelligence == 2:
                                    x = 60 + coef
                                if intelligence == 3:
                                    x = 40 + coef
                                if intelligence == 4:
                                    x = 20 + coef
                                if x >= 90:
                                    x = 90
                                if random.randint(1, 100) <= x:
                                    cardplayers.remove(ids[1])
                                else:
                                    cardplayers.remove(ids[0])
                                i = 10

                        except:
                            try:
                                print('try3')
                                int(ids[1])
                                index = 0
                                coef = 0
                                user = users.find_one({'id': ids[1]})
                                if user != None:
                                    coef += user['intelligence']
                                if ids[index] == 'miku':
                                    intelligence = mikustats['intelligence']
                                if ids[index] == 'alisa':
                                    intelligence = alisastats['intelligence']
                                if ids[index] == 'lena':
                                    intelligence = lenastats['intelligence']
                                if ids[index] == 'slavya':
                                    intelligence = slavyastats['intelligence']
                                if ids[index] == 'zhenya':
                                    intelligence = zhenyastats['intelligence']
                                if ids[index] == 'uliana':
                                    intelligence = ulianastats['intelligence']
                                if intelligence == 1:
                                    x = 75 + coef
                                if intelligence == 2:
                                    x = 60 + coef
                                if intelligence == 3:
                                    x = 40 + coef
                                if intelligence == 4:
                                    x = 20 + coef
                                if x >= 90:
                                    x = 90
                                if random.randint(1, 100) <= x:
                                    cardplayers.remove(ids[0])
                                else:
                                    cardplayers.remove(ids[1])
                                i = 10

                            except:
                                print('try4')
                                if ids[0] == 'miku':
                                    intelligence1 = mikustats['intelligence']
                                if ids[0] == 'alisa':
                                    intelligence1 = alisastats['intelligence']
                                if ids[0] == 'lena':
                                    intelligence1 = lenastats['intelligence']
                                if ids[0] == 'slavya':
                                    intelligence1 = slavyastats['intelligence']
                                if ids[0] == 'zhenya':
                                    intelligence1 = zhenyastats['intelligence']
                                if ids[0] == 'uliana':
                                    intelligence1 = ulianastats['intelligence']
                                if ids[1] == 'miku':
                                    intelligence2 = mikustats['intelligence']
                                if ids[1] == 'alisa':
                                    intelligence2 = alisastats['intelligence']
                                if ids[1] == 'lena':
                                    intelligence2 = lenastats['intelligence']
                                if ids[1] == 'slavya':
                                    intelligence2 = slavyastats['intelligence']
                                if ids[1] == 'zhenya':
                                    intelligence2 = zhenyastats['intelligence']
                                if ids[1] == 'uliana':
                                    intelligence2 = ulianastats['intelligence']
                                z = intelligence1 - intelligence2
                                if z == 0:
                                    x = 50
                                elif z == 1:
                                    x = 60
                                elif z == 2:
                                    x = 75
                                elif z == 3:
                                    x = 85
                                elif z == -1:
                                    x = 40
                                elif z == -2:
                                    x = 25
                                elif z == -3:
                                    x = 15
                                if random.randint(1, 100) <= x:
                                    cardplayers.remove(ids[1])
                                else:
                                    cardplayers.remove(ids[0])
                                i = 10
            text = ''
            x = 0
            for dd in cardplayers:
                x += 1
                try:
                    int(dd)
                    text += users.find_one({'id': dd})['pionername'] + '\n'
                except:
                    text += nametopioner(dd) + '\n'
            text1 = ''
            text3 = ''
            if electronicstats['cardsturn'] == 1:
                text1 = 'Завершился первый этап турнира! А вот и наши победители:\n\n'
            elif electronicstats['cardsturn'] == 2:
                if x > 1:
                    text1 = 'Второй этап турнира подошёл к концу! Встречайте победителей:\n\n'
                else:
                    text1 = 'Финал подошёл к концу! И наш победитель:\n\n'
            elif electronicstats['cardsturn'] == 3:
                if x == 2:
                    text1 = 'Полуфинал завершён! В финале встретятся:\n\n'
                else:
                    text1 = 'Встречайте победителя турнира:\n\n'
            elif electronicstats['cardsturn'] == 4:
                text1 = 'Турнир завершён! И наш победитель:\n\n'
            if x == 2:
                text3 = 'Настало время для финала! Кто же станет победителем на этот раз?'
            elif x == 4:
                text3 = 'На очереди у нас полуфинал. Кто же из четырёх оставшихся игроков попадёт в финал?'
            elif x == 8:
                text3 = 'Скоро начнётся раунд 2. Игроки, приготовьтесь!'
            electronicstats['cardsturn'] += 1
            electronic.send_message(-1001351496983, text1 + text + '\n' + text3, parse_mode='markdown')
            setka = []
            i = 0
            if len(cardplayers) > 1:
                x = len(cardplayers) / 2
                while i < x:
                    player1 = random.choice(cardplayers)
                    cardplayers.remove(player1)
                    player2 = random.choice(cardplayers)
                    cardplayers.remove(player2)
                    lst = [player1, player2]
                    setka.append(lst)
                    i += 1
                t = threading.Timer(120, cards_nextturn)
                t.start()
            else:
                time.sleep(2)
                bot.send_chat_action(-1001351496983, 'typing')
                time.sleep(5)
                try:
                    name = users.find_one({'id': cardplayers[0]})['pionername']
                except:
                    name = nametopioner(cardplayers[0])
                bot.send_message(-1001351496983,
                                 'Отлично! Поздравляю, ' + name + '! А теперь приберитесь тут, скоро ужин.',
                                 parse_mode='markdown')
                bot.send_sticker(-1001351496983, 'CAADAgADqwADgi0zDzm_zSmMbMmiAg')
                setka = []
                cardplayers = []
                electronicstats['waitingplayers'] = 0
                electronicstats['playingcards'] = 0
                electronicstats['cardsturn'] = 0
        else:
            electronic.send_message(-1001351496983,
                                    'К сожалению, игроков для турнира сегодня не набралось. Ну ничего, в следующий раз попробуем!')
            setka = []
            cardplayers = []
            electronicstats['waitingplayers'] = 0
            electronicstats['playingcards'] = 0
            electronicstats['cardsturn'] = 0

    except:
        setka = []
        cardplayers = []
        electronicstats['waitingplayers'] = 0
        electronicstats['playingcards'] = 0
        electronicstats['cardsturn'] = 0
        electronic.send_message(-1001351496983, 'Непредвиденные обстоятельства! Турнир придётся отменить!')


def talkwithplayer(player, pioner):
    if pioner == 'miku':
        t = threading.Timer(random.randint(10, 90), sayto, args=[miku, 'miku', player, cards_startround_mikutexts])
        t.start()
    if pioner == 'alisa':
        t = threading.Timer(random.randint(10, 90), sayto, args=[alisa, 'alisa', player, cards_startround_alisatexts])
        t.start()
    if pioner == 'zhenya':
        t = threading.Timer(random.randint(10, 90), sayto,
                            args=[zhenya, 'zhenya', player, cards_startround_zhenyatexts])
        t.start()
    if pioner == 'uliana':
        t = threading.Timer(random.randint(10, 90), sayto,
                            args=[uliana, 'uliana', player, cards_startround_ulianatexts])
        t.start()
    if pioner == 'slavya':
        t = threading.Timer(random.randint(10, 90), sayto,
                            args=[slavya, 'slavya', player, cards_startround_slavyatexts])
        t.start()
    if pioner == 'lena':
        t = threading.Timer(random.randint(10, 90), sayto, args=[lena, 'lena', player, cards_startround_lenatexts])
        t.start()


cards_startround_mikutexts = ['Ой, Привет! Если не помнишь, то меня Мику зовут. Мы сейчас с тобой ' + \
                              'играем! Ты хорошо играешь? Я не очень...',
                              'Привет! Мы с тобой уже знакомы, если помнишь... ' + \
                              'Удачи на турнире!']
cards_startround_alisatexts = ['Ну привет. Готовься проиграть!']
cards_startround_slavyatexts = ['Привет! Интересно, кто победит в турнире в этот раз...']
cards_startround_ulianatexts = ['Привет-привет! Я сегодня настроена на победу, так что советую сразу сдаться!']
cards_startround_lenatexts = ['Привет. Удачи на сегодняшнем турнире!']
cards_startround_zhenyatexts = ['Выходит, мы с тобой сегодня играем. Давай сразу к игре, без лишних разговоров!']


def sayto(pioner, pionername, id, texts):
    x = users.find_one({'id': id})
    if x['gender'] == 'female':
        gndr = 'а'
    else:
        gndr = ''
    if pionername == 'miku':
        textstochat = ['Привет, ' + x['pionername'] + '! Меня Мику зовут! Мы ещё не знакомы, можем ' + \
                       '[поговорить](https://t.me/ES_MikuBot) после турнира... А сейчас - удачи!']
    elif pionername == 'alisa':
        textstochat = ['Ну привет, ' + x['pionername'] + '! Думаешь победить в турнире? Даже не надейся! Меня тебе ' + \
                       'точно не обыграть!']
    elif pionername == 'slavya':
        textstochat = ['Привет, ' + x['pionername'] + '! Чего-то я тебя не видела раньше... Меня Славя зовут! Можем ' + \
                       '[познакомиться](https://t.me/SlavyaBot) на досуге. Ну а сейчас готовься к игре!']
    elif pionername == 'uliana':
        textstochat = ['Привет! Тебя ведь ' + x['pionername'] + ' зовут? Я Ульяна! Готов' + gndr + ' проиграть?']

    elif pionername == 'lena':
        textstochat = ['Привет, ' + x[
            'pionername'] + '. Меня Лена зовут... Хотя ты наверняка уже знаешь, ведь в турнирной сетке написано. ' + \
                       'Удачи!']

    elif pionername == 'zhenya':
        textstochat = ['Ну привет, ' + x['pionername'] + '. Не знаю, зачем я вообще играю, но уже поздно передумывать.']

    try:
        pioner.send_chat_action(id, 'typing')
        time.sleep(5)
        pioner.send_message(id, random.choice(texts))
    except:
        pioner.send_chat_action(-1001351496983, 'typing')
        time.sleep(5)
        pioner.send_message(-1001351496983, random.choice(textstochat), parse_mode='markdown')


def nametopioner(pioner):
    if pioner == 'miku':
        return '[Мику](https://t.me/ES_MikuBot)'
    if pioner == 'alisa':
        return '[Алиса](https://t.me/ES_AlisaBot)'
    if pioner == 'zhenya':
        return '[Женя](https://t.me/ES_ZhenyaBot)'
    if pioner == 'uliana':
        return '[Ульяна](https://t.me/ES_UlianaBot)'
    if pioner == 'slavya':
        return '[Славя](https://t.me/SlavyaBot)'
    if pioner == 'lena':
        return '[Лена](https://t.me/ES_LenaBot)'
    if pioner == 'electronic':
        return '[Электроник](https://t.me/ES_ElectronicBot)'
    if pioner == 'shurik':
        return '[Шурик](https://t.me/Shurgen_bot)'


def addtogame(name, game):
    game.append(name)


def sendmes(sender, text, parse_mode):
    sender.send_message(-1001351496983, text, parse_mode=parse_mode)


def sendstick(sender, stick):
    sender.send_sticker(-1001351496983, stick)


####################################### ELECTRONIC ##############################################
@electronic.message_handler(commands=['control'])
def electroniccontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in el_admins:
        if electronicstats['controller'] == None:
            electronicstats['controller'] = {'id': m.from_user.id,
                                             'name': m.from_user.first_name}
            electronic.send_message(m.from_user.id, 'Привет! надеюсь ты знаешь, как управлять мной.')
        else:
            electronic.send_message(m.from_user.id, 'Мной уже управляет ' + electronicstats['controller']['name'] + '!')


@electronic.message_handler(commands=['stopcontrol'])
def electronicstopcontrol(m):
    if electronicstats['controller'] != None:
        if electronicstats['controller']['id'] == m.from_user.id:
            electronicstats['controller'] = None
            electronic.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@electronic.message_handler(content_types=['sticker'])
def stickercatchelectronic(m):
    stickhandler(m, electronic)


@electronic.message_handler()
def electronichandler(m):
    try:
        if ban.find_one({'id': m.from_user.id}) == None:
            if electronicstats['waitingplayers'] == 1:
                if m.text.lower() == 'хочу принять участие в турнире!':
                    x = users.find_one({'id': m.from_user.id})
                    if x['gender'] == 'female':
                        gndr = 'а'
                    else:
                        gndr = ''
                    if x['id'] not in cardplayers:
                        if m.from_user.id == m.chat.id:
                            texts = ['Привет! Записал тебя в список участников. Жди начала турнира!',
                                     'Хорошо. Записал тебя!',
                                     'Рад, что тебя заинтересовала моя игра. Теперь ты тоже в списке участников!']
                            text = random.choice(texts)
                            electronic.send_message(m.chat.id, text)
                            cardplayers.append(x['id'])
                        else:
                            if m.reply_to_message != None:
                                if m.reply_to_message.from_user.id == 609648686:
                                    texts = ['Привет, [' + x['pionername'] + '](tg://user?id=' + str(
                                        x['id']) + ')! Записал тебя в список участников. Жди начала турнира!',
                                             'Хорошо, [' + x['pionername'] + '](tg://user?id=' + str(
                                                 x['id']) + '). Записал тебя!',
                                             'Рад, что тебя заинтересовала моя игра. Теперь ты тоже в списке участников!']
                                    text = random.choice(texts)
                                    electronic.send_message(m.chat.id, text, parse_mode='markdown',
                                                            reply_to_message_id=m.message_id)
                                    cardplayers.append(x['id'])
                    else:
                        if m.from_user.id == m.chat.id:
                            reply_to_message_id = None
                        else:
                            reply_to_message_id = m.message_id
                        electronic.send_message(m.chat.id, '[' + x['pionername'] + '](tg://user?id=' + str(x['id']) + \
                                                '), ты уже записан' + gndr + ' на турнир!', parse_mode='markdown',
                                                reply_to_message_id=reply_to_message_id)
                else:
                    pass

            msghandler(m, electronic)

    except:
        electronic.send_message(441399484, traceback.format_exc())


@lena.message_handler(commands=['control'])
def lenacontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in le_admins:
        if lenastats['controller'] == None:
            lenastats['controller'] = {'id': m.from_user.id,
                                       'name': m.from_user.first_name}
            lena.send_message(m.from_user.id,
                              'Теперь ты управляешь мной! Я буду присылать тебе все сообщения, которые вижу!')
        else:
            lena.send_message(m.from_user.id, 'Мной уже управляет ' + lenastats['controller']['name'] + '!')


@lena.message_handler(commands=['stopcontrol'])
def lenastopcontrol(m):
    if lenastats['controller'] != None:
        if lenastats['controller']['id'] == m.from_user.id:
            lenastats['controller'] = None
            lena.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@lena.message_handler()
def lenamessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        print('1')
        yes = ['да!', 'конечно!', 'да', 'да, могу.', 'могу', 'могу.', 'конечно могу!', 'да']
        if lenastats['whohelps'] != None:
            print('2')
            y = 0
            if m.from_user.id == lenastats['whohelps']:
                print('3')
                for ids in yes:
                    if ids in m.text.lower():
                        y = 1
                if y == 1:
                    pioner = users.find_one({'id': m.from_user.id})
                    print('4')
                    try:
                        lenastats['timer'].cancel()
                    except:
                        pass
                    allhelps = ['Спасибо! Тогда пошли, мне нужно отсортировать лекарства в медпункте.',
                                'Спасибо! Пойдём, надо разобрать склад и принести несколько комплектов пионерской формы для Слави.']
                    lenastats['whohelps'] = None
                    helpp = random.choice(allhelps)
                    lena.send_chat_action(m.chat.id, 'typing')
                    time.sleep(4)
                    lena.send_message(m.chat.id, helpp)
                    sendstick(lena, 'CAADAgADZwADgi0zD-vRcG90IHeAAg')
                    t = threading.Timer(300, helpend, args=[m.from_user.id, 'lena'])
                    t.start()
                    users.update_one({'id': m.from_user.id}, {'$set': {'helping': 1}})
        msghandler(m, lena)


@lena.message_handler(content_types=['sticker'])
def stickercatchlena(m):
    stickhandler(m, lena)


####################################### ALICE ##############################################
@alisa.message_handler(commands=['control'])
def alisacontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in al_admins:
        if alisastats['controller'] == None:
            alisastats['controller'] = {'id': m.from_user.id,
                                        'name': m.from_user.first_name}
            alisa.send_message(m.from_user.id,
                               'Ну ты вроде теперь мной управляешь. Я буду присылать тебе все сообщения, которые вижу, но если мне что-то не понравится - буду злиться!')
        else:
            alisa.send_message(m.from_user.id, 'Мной уже управляет ' + alisastats['controller']['name'] + '!')


@alisa.message_handler(commands=['stopcontrol'])
def alisastopcontrol(m):
    if alisastats['controller'] != None:
        if alisastats['controller']['id'] == m.from_user.id:
            alisastats['controller'] = None
            alisa.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@alisa.message_handler()
def alisamessages(m):
    try:
        if ban.find_one({'id': m.from_user.id}) == None:
            yes = ['да', 'я готов', 'го', 'ну го', 'я в деле']
            if alisastats['whohelps'] != None:
                y = 0
                try:
                    bot.send_message(441399484, str(alisastats['whohelps']))
                except:
                    bot.send_message(441399484, traceback.format_exc())
                if m.from_user.id == alisastats['whohelps']:
                    for ids in yes:
                        if ids in m.text.lower():
                            y = 1
                    if y == 1:
                        bot.send_message(441399484, '1')
                        pioner = users.find_one({'id': m.from_user.id})
                        try:
                            alisastats['timer'].cancel()
                        except:
                            pass
                        allhelps = ['Ну пошли, там нужно один прикол с Электроником намутить...',
                                    'Отлично! Значит так, нам с Ульяной нужен отвлекающий на кухню...']
                        alisastats['whohelps'] = None
                        helpp = random.choice(allhelps)
                        alisa.send_chat_action(m.chat.id, 'typing')
                        time.sleep(4)
                        alisa.send_message(m.chat.id, helpp)
                        sendstick(alisa, 'CAADAgADOwADgi0zDzD8ZNZXu5LHAg')
                        t = threading.Timer(300, helpend, args=[m.from_user.id, 'alisa'])
                        t.start()
                        users.update_one({'id': m.from_user.id}, {'$set': {'helping': 1}})

            msghandler(m, alisa)
            if m.chat.id == mainchat:
                if m.reply_to_message != None:
                    if m.reply_to_message.from_user.id == 634115873:
                        pioner = users.find_one({'id': m.from_user.id})
                        if pioner != None:
                            text = m.text.lower()
                            if 'пошли' in text:
                                if 'ко мне' in text:
                                    texts2 = ['Ну... Я подумаю.', 'Даже не знаю...']
                                    texts1 = ['Совсем офигел?', 'Страх потерял?']
                                    texts3 = ['Лучше ко мне', 'Ну пошли!']
                                    stick2 = 'CAADAgAD4QIAAnHMfRgPhIdIfUrCGAI'
                                    stick1 = 'CAADAgAD4wIAAnHMfRjkcHoZL5eAgwI'
                                    stick3 = 'CAADAgAD7AIAAnHMfRgXuTTXBIbwWgI'
                                    if pioner['Alisa_respect'] < 40:
                                        txt = texts1
                                        stick = stick1
                                    elif pioner['Alisa_respect'] <= 50:
                                        txt = texts2
                                        stick = stick2
                                    elif pioner['Alisa_respect'] <= 75:
                                        txt = texts3
                                        stick = stick3
                                    alisa.send_chat_action(mainchat, 'typing')
                                    t = threading.Timer(3, sendmes, args=[alisa, random.choice(txt), None])
                                    t.start()
                                    t = threading.Timer(3, sendstick, args=[alisa, stick])
                                    t.start()

    except:
        alisa.send_message(441399484, traceback.format_exc())


@alisa.message_handler(content_types=['sticker'])
def stickercatchalisa(m):
    stickhandler(m, alisa)


####################################### ULIANA ##############################################
@uliana.message_handler(commands=['control'])
def ulianaacontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in ul_admins:
        if ulianastats['controller'] == None:
            ulianastats['controller'] = {'id': m.from_user.id,
                                         'name': m.from_user.first_name}
            uliana.send_message(m.from_user.id, 'Привет! Теперь ты мной управляешь, прикольно!')
        else:
            uliana.send_message(m.from_user.id, 'Мной уже управляет ' + ulianastats['controller']['name'] + '!')


@uliana.message_handler(commands=['stopcontrol'])
def ulianastopcontrol(m):
    if ulianastats['controller'] != None:
        if ulianastats['controller']['id'] == m.from_user.id:
            ulianastats['controller'] = None
            uliana.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@uliana.message_handler()
def ulianamessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        yes = ['да', 'давай', 'я в деле', 'рассказывай']
        if ulianastats['whohelps'] != None:
            y = 0
            if m.from_user.id == ulianastats['whohelps']:
                for ids in yes:
                    if ids in m.text.lower():
                        y = 1
                if y == 1:
                    pioner = users.find_one({'id': m.from_user.id})
                    try:
                        ulianastats['timer'].cancel()
                    except:
                        pass
                    allhelps = [
                        'Я тут хочу заняться одним безобидным делом, и в этом мне потребуются спички... Если что, тебя не сдам!',
                        'О, круто! Мне тут нужно раздобыть немного глицерина...']
                    ulianastats['whohelps'] = None
                    helpp = random.choice(allhelps)
                    uliana.send_chat_action(m.chat.id, 'typing')
                    time.sleep(4)
                    uliana.send_message(m.chat.id, helpp)
                    sendstick(uliana, 'CAADAgADKQADgi0zD_inNy0pZyh0Ag')
                    t = threading.Timer(300, helpend, args=[m.from_user.id, 'uliana'])
                    t.start()
                    users.update_one({'id': m.from_user.id}, {'$set': {'helping': 1}})
        msghandler(m, uliana)


@uliana.message_handler(content_types=['sticker'])
def stickercatchalisa(m):
    stickhandler(m, uliana)


####################################### SLAVYA ##############################################
@slavya.message_handler(commands=['control'])
def slavyacontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in sl_admins:
        if slavyastats['controller'] == None:
            slavyastats['controller'] = {'id': m.from_user.id,
                                         'name': m.from_user.first_name}
            slavya.send_message(m.from_user.id, 'Привет! Теперь ты мной управляешь! Только аккуратнее!')
        else:
            slavya.send_message(m.from_user.id, 'Мной уже управляет ' + slavyastats['controller']['name'] + '!')


@slavya.message_handler(commands=['stopcontrol'])
def slavyastopcontrol(m):
    if slavyastats['controller'] != None:
        if slavyastats['controller']['id'] == m.from_user.id:
            slavyastats['controller'] = None
            slavya.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@slavya.message_handler()
def slavyamessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        yes = ['да', 'я готов', 'давай', 'я в деле']
        if slavyastats['whohelps'] != None:
            y = 0
            if m.from_user.id == slavyastats['whohelps']:
                for ids in yes:
                    if ids in m.text.lower():
                        y = 1
                if y == 1:
                    pioner = users.find_one({'id': m.from_user.id})
                    try:
                        slavyastats['timer'].cancel()
                    except:
                        pass
                    allhelps = [
                        'Отлично! А теперь само задание: надо развесить на деревьях гирлянды, а то завтра вечером будут танцы! Нужна соответствующая атмосфера.',
                        'Спасибо! Тогда наполни вот это ведро водой и принеси сюда, мне надо помыть памятник.']
                    slavyastats['whohelps'] = None
                    helpp = random.choice(allhelps)
                    slavya.send_chat_action(m.chat.id, 'typing')
                    time.sleep(4)
                    slavya.send_message(m.chat.id, helpp)
                    sendstick(slavya, 'CAADAgADUgADgi0zD4hu1wGvwGllAg')
                    t = threading.Timer(300, helpend, args=[m.from_user.id, 'slavya'])
                    t.start()
                    users.update_one({'id': m.from_user.id}, {'$set': {'helping': 1}})
        msghandler(m, slavya)


@slavya.message_handler(content_types=['sticker'])
def stickercatchslavya(m):
    stickhandler(m, slavya)


####################################### MIKU ##############################################
@miku.message_handler(commands=['control'])
def mikucontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in mi_admins:
        if mikustats['controller'] == None:
            mikustats['controller'] = {'id': m.from_user.id,
                                       'name': m.from_user.first_name}
            miku.send_message(m.from_user.id,
                              'Привет! Теперь ты управляешь мной, как здорово! Ой, а я однажды в школе пыталась управлять музыкальным клубом, но ничего не вышло... Надеюсь, у тебя получится лучше!')
        else:
            miku.send_message(m.from_user.id, 'Мной уже управляет ' + mikustats['controller']['name'] + '!')


@miku.message_handler(commands=['stopcontrol'])
def mikustopcontrol(m):
    if mikustats['controller'] != None:
        if mikustats['controller']['id'] == m.from_user.id:
            mikustats['controller'] = None
            miku.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@miku.message_handler()
def mikumessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        msghandler(m, miku)


@miku.message_handler(content_types=['sticker'])
def stickercatchmiku(m):
    stickhandler(m, miku)

####################################### ZHENYA ##############################################
@zhenya.message_handler(commands=['control'])
def zhenyacontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in zh_admins:
        if zhenyastats['controller'] == None:
            zhenyastats['controller'] = {'id': m.from_user.id,
                                         'name': m.from_user.first_name}
            zhenya.send_message(m.from_user.id, 'Привет, ты теперь управляешь мной... А я пока пойду почитаю.')
        else:
            zhenya.send_message(m.from_user.id, 'Мной уже управляет ' + zhenyastats['controller']['name'] + '!')


@zhenya.message_handler(commands=['stopcontrol'])
def zhenyastopcontrol(m):
    if zhenyastats['controller'] != None:
        if zhenyastats['controller']['id'] == m.from_user.id:
            zhenyastats['controller'] = None
            zhenya.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@zhenya.message_handler()
def zhenyamessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        msghandler(m, zhenya)


@zhenya.message_handler(content_types=['sticker'])
def stickercatchzhenya(m):
    stickhandler(m, zhenya)


####################################### TOLIK ##############################################
@tolik.message_handler(commands=['control'])
def tolikcontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in to_admins:
        if tolikstats['controller'] == None:
            tolikstats['controller'] = {'id': m.from_user.id,
                                        'name': m.from_user.first_name}
            tolik.send_message(m.from_user.id, 'Я - Толик.')
        else:
            tolik.send_message(m.from_user.id, 'Мной уже управляет ' + tolikstats['controller']['name'] + '!')


@tolik.message_handler(commands=['stopcontrol'])
def tolikstopcontrol(m):
    if tolikstats['controller'] != None:
        if tolikstats['controller']['id'] == m.from_user.id:
            tolikstats['controller'] = None
            tolik.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@tolik.message_handler()
def tolikmessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        msghandler(m, tolik)


@tolik.message_handler(content_types=['sticker'])
def stickercatchtolik(m):
    stickhandler(m, tolik)


####################################### SHURIK ##############################################
@shurik.message_handler(commands=['control'])
def shurikcontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in sh_admins:
        if shurikstats['controller'] == None:
            shurikstats['controller'] = {'id': m.from_user.id,
                                         'name': m.from_user.first_name}
            shurik.send_message(m.from_user.id, 'Привет, ну ты теперь управляешь мной. Думаю, что умеешь.')
        else:
            shurik.send_message(m.from_user.id, 'Мной уже управляет ' + shurikstats['controller']['name'] + '!')


@shurik.message_handler(commands=['stopcontrol'])
def shuriktopcontrol(m):
    if shurikstats['controller'] != None:
        if shurikstats['controller']['id'] == m.from_user.id:
            shurikstats['controller'] = None
            shurik.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@shurik.message_handler()
def shurikmessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        msghandler(m, shurik)


@shurik.message_handler(content_types=['sticker'])
def stickercatchzshurik(m):
    stickhandler(m, shurik)

            ###################################### SEMEN ###############################################


@semen.message_handler(commands=['control'])
def semencontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in se_admins:
        if semenstats['controller'] == None:
            semenstats['controller'] = {'id': m.from_user.id,
                                        'name': m.from_user.first_name}
            semen.send_message(m.from_user.id, 'Ну ты типо мной управляешь.')
        else:
            semen.send_message(m.from_user.id, 'Мной уже управляет ' + semenstats['controller']['name'] + '!')


@semen.message_handler(commands=['stopcontrol'])
def semenstopcontrol(m):
    if semenstats['controller'] != None:
        if semenstats['controller']['id'] == m.from_user.id:
            semenstats['controller'] = None
            semen.send_message(m.from_user.id, 'Ты больше не управляешь мной!')


@semen.message_handler()
def semenmessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        msghandler(m, semen)


@semen.message_handler(content_types=['sticker'])
def stickercatchsemen(m):
    stickhandler(m, semen)

            ###################################### PIONEER ###############################################


@pioneer.message_handler(commands=['control'])
def pioneercontrol(m):
    if m.from_user.id in botadmins or m.from_user.id in pi_admins:
        if pioneerstats['controller'] == None:
            pioneerstats['controller'] = {'id': m.from_user.id,
                                          'name': m.from_user.first_name}
            pioneer.send_message(m.from_user.id, 'Хех, посмотрим, что ты придумал.')
        else:
            pioneer.send_message(m.from_user.id, 'Мной управляет ' + pioneerstats['controller']['name'] + '.')


@pioneer.message_handler(commands=['stopcontrol'])
def pioneerstopcontrol(m):
    if pioneerstats['controller'] != None:
        if pioneerstats['controller']['id'] == m.from_user.id:
            pioneerstats['controller'] = None
            pioneer.send_message(m.from_user.id, 'Ты больше не управляешь мной.')


@pioneer.message_handler()
def pioneermessages(m):
    if ban.find_one({'id': m.from_user.id}) == None:
        msghandler(m, pioneer)


@pioneer.message_handler(content_types=['sticker'])
def stickercatchpioneer(m):
    stickhandler(m, pioneer)


def helpend(id, pioner):
    x = users.find_one({'id': id})
    users.update_one({'id': id}, {'$set': {'helping': 0}})
    if pioner == 'lena':
        lena.send_chat_action(id, 'typing')
        time.sleep(4)
        lena.send_message(-1001351496983,
                          'Спасибо за помощь, [' + x['pionername'] + '](tg://user?id=' + str(x['id']) + ')! ' + \
                          'Без тебя ушло бы гораздо больше времени. Ну, я пойду...', parse_mode='markdown')
        users.update_one({'id': x['id']}, {'$inc': {'Lena_respect': random.randint(4, 5)}})
    if pioner == 'alisa':
        alisa.send_chat_action(id, 'typing')
        time.sleep(4)
        alisa.send_message(-1001351496983,
                           'Ну спасибо за помощь, [' + x['pionername'] + '](tg://user?id=' + str(x['id']) + ')! ' + \
                           'Неплохо получилось!', parse_mode='markdown')
        users.update_one({'id': x['id']}, {'$inc': {'Alisa_respect': random.randint(4, 5)}})

    if pioner == 'slavya':
        slavya.send_chat_action(id, 'typing')
        time.sleep(4)
        slavya.send_message(-1001351496983,
                            'Спасибо за помощь, [' + x['pionername'] + '](tg://user?id=' + str(x['id']) + ')! ' + \
                            'Теперь можешь отдыхать.', parse_mode='markdown')
        users.update_one({'id': x['id']}, {'$inc': {'Slavya_respect': random.randint(4, 5)}})

    if pioner == 'uliana':
        uliana.send_chat_action(id, 'typing')
        time.sleep(4)
        uliana.send_message(-1001351496983,
                            'Как здорово! Спасибо за помощь, [' + x['pionername'] + '](tg://user?id=' + str(
                                x['id']) + ')!' + \
                            '', parse_mode='markdown')
        users.update_one({'id': x['id']}, {'$inc': {'Uliana_respect': random.randint(4, 5)}})


cardplayers = []

alisastats = {
    'strenght': 1,
    'agility': 2,
    'intelligence': 3,
    'controller': None,
    'bot': alisa,
    'whohelps': None
}
lenastats = {
    'strenght': 2,
    'agility': 2,
    'intelligence': 2,
    'whohelps': None,
    'timer': None,
    'controller': None,
    'bot': lena
}
mikustats = {
    'strenght': 2,
    'agility': 2,
    'intelligence': 2,
    'controller': None,
    'bot': miku
}
ulianastats = {
    'strenght': 1,
    'agility': 4,
    'intelligence': 1,
    'controller': None,
    'bot': uliana,
    'whohelps': None,
    'timer': None
}
slavyastats = {
    'strenght': 1,
    'agility': 1,
    'whohelps': None,
    'timer': None,
    'intelligence': 4,
    'controller': None,
    'bot': slavya
}
electronicstats = {
    'strenght': 3,
    'agility': 1,
    'intelligence': 4,
    'waitingplayers': 0,
    'playingcards': 0,
    'cardsturn': 0,
    'controller': None,
    'bot': electronic

}
zhenyastats = {
    'strenght': 2,
    'agility': 1,
    'intelligence': 3,
    'controller': None,
    'bot': zhenya

}

tolikstats = {
    'strenght': 2,
    'agility': 2,
    'intelligence': 2,
    'controller': None,
    'bot': tolik

}

shurikstats = {
    'strenght': 2,
    'agility': 1,
    'intelligence': 4,
    'controller': None,
    'bot': shurik

}

odstats = {
    'lineyka': [],
    'waitforlineyka': 0,
    'controller': None,
    'bot': bot
}

semenstats = {
    'controller': None,
    'bot': semen
}

pioneerstats = {
    'controller': None,
    'bot': pioneer
}

ctrls = []
ctrls.append(odstats)
ctrls.append(electronicstats)
ctrls.append(slavyastats)
ctrls.append(zhenyastats)
ctrls.append(ulianastats)
ctrls.append(mikustats)
ctrls.append(lenastats)
ctrls.append(alisastats)
ctrls.append(shurikstats)
ctrls.append(tolikstats)

zavtrak = '9:00'
obed = '14:00'
uzhin = '21:00'


def findindex(x):
    i = 0
    for ids in works:
        if ids['name'] == x:
            index = i
        i += 1
    return index


def randomhelp():
    t = threading.Timer(random.randint(420, 1000), randomhelp)
    t.start()
    global rds
    if rds == True:
        spisok = []
        pioners = ['lena', 'alisa', 'slavya', 'uliana']
        x = users.find({})
        for ids in x:
            if ids['pionername'] != None:
                spisok.append(ids)
        if len(spisok) > 0:
            hour = gettime('h')
            if hour >= 7 and hour <= 23:
                pioner = random.choice(spisok)
                z = random.choice(pioners)
                helpto(pioner, z)


def helpto(pioner, x):
    if pioner['gender'] == 'male':
        g = ''
    else:
        g = 'ла'
    if x == 'lena':
        try:
            if pioner['Lena_respect'] >= 85:
                text = '[' + pioner['pionername'] + '](tg://user?id=' + str(pioner[
                                                                                'id']) + '), привет! Ты мне часто помогаешь, поэтому хотелось бы попросить тебя о помощи еще раз... Не откажешь?'
            else:
                text = '[' + pioner['pionername'] + '](tg://user?id=' + str(
                    pioner['id']) + '), привет. Не мог' + g + ' бы ты мне помочь?'
            lena.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            m = lena.send_message(-1001351496983, text, parse_mode='markdown')
            lenastats['whohelps'] = pioner['id']
            t = threading.Timer(300, helpcancel, args=['lena', m, pioner['id']])
            t.start()
            lenastats['timer'] = t
            sendstick(lena, 'CAADAgADaQADgi0zD9ZBO-mNcLuBAg')
        except:
            pass

    if x == 'alisa':
        try:
            if pioner['Alisa_respect'] >= 85:
                text = '[' + pioner['pionername'] + '](tg://user?id=' + str(
                    pioner['id']) + '), привет, я же знаю, что ты любишь повеселиться! Готов на этот раз?'
            else:
                text = '[' + pioner['pionername'] + '](tg://user?id=' + str(pioner[
                                                                                'id']) + '), смотри, куда идёшь! Должен будешь, и долг отработаешь прямо сейчас. Мне тут помощь нужна в одном деле...'
            alisa.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            m = alisa.send_message(-1001351496983, text, parse_mode='markdown')
            alisastats['whohelps'] = pioner['id']
            t = threading.Timer(300, helpcancel, args=['alisa', m, pioner['id']])
            t.start()
            alisastats['timer'] = t
            sendstick(alisa, 'CAADAgADOQADgi0zDztSbkeWq3BEAg')
        except:
            bot.send_message(441399484, traceback.format_exc())

    if x == 'slavya':
        try:
            if pioner['Slavya_respect'] >= 85:
                text = 'Привет, ' + '[' + pioner['pionername'] + '](tg://user?id=' + str(pioner[
                                                                                             'id']) + ')! Ты не раз выручал меня, поэтому я знаю, что тебе можно довериться. Поможешь мне с одним важным заданием?'
            else:
                text = 'Привет, [' + pioner['pionername'] + '](tg://user?id=' + str(
                    pioner['id']) + ')! Поможешь мне с одним важным заданием?'
            slavya.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            m = slavya.send_message(-1001351496983, text, parse_mode='markdown')
            slavyastats['whohelps'] = pioner['id']
            t = threading.Timer(300, helpcancel, args=['slavya', m, pioner['id']])
            t.start()
            slavyastats['timer'] = t
            sendstick(slavya, 'CAADAgADTAADgi0zD6PLpc722Bz3Ag')
        except:
            bot.send_message(441399484, traceback.format_exc())

    if x == 'uliana':
        try:
            if pioner['Uliana_respect'] >= 85:
                text = 'Привет, ' + '[' + pioner['pionername'] + '](tg://user?id=' + str(
                    pioner['id']) + ')! Мне не помешала бы помощь в одном деле... Я знаю, что ты согласишься!'
            else:
                text = 'Эй, [' + pioner['pionername'] + '](tg://user?id=' + str(
                    pioner['id']) + ')! Поможешь мне с одним делом?'
            uliana.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            m = uliana.send_message(-1001351496983, text, parse_mode='markdown')
            ulianastats['whohelps'] = pioner['id']
            t = threading.Timer(300, helpcancel, args=['uliana', m, pioner['id']])
            t.start()
            ulianastats['timer'] = t
            sendstick(uliana, 'CAADAgADLwADgi0zD7_x8Aph94DmAg')
        except:
            bot.send_message(441399484, traceback.format_exc())


def helpcancel(pioner, m, userid):
    user = users.find_one({'id': userid})
    if pioner == 'lena':
        lenastats['whohelps'] = None
        lena.send_chat_action(-1001351496983, 'typing')
        time.sleep(4)
        lena.send_message(-1001351496983, 'Ты, наверное, сейчас занят... Прости, что побеспокоила.',
                          reply_to_message_id=m.message_id)
        if user['Lena_respect'] > 0:
            users.update_one({'id': user['id']}, {'$inc': {'Lena_respect': -1}})
    if pioner == 'alisa':
        alisastats['whohelps'] = None
        alisa.send_chat_action(-1001351496983, 'typing')
        time.sleep(4)
        if user['Alisa_respect'] < 85:
            alisa.send_message(-1001351496983, 'Ну и пожалуйста!', reply_to_message_id=m.message_id)
        else:
            alisa.send_message(-1001351496983, 'Ну как хочешь! Сама справлюсь.', reply_to_message_id=m.message_id)
        if user['Alisa_respect'] > 0:
            users.update_one({'id': user['id']}, {'$inc': {'Alisa_respect': -1}})
    if pioner == 'slavya':
        slavyastats['whohelps'] = None
        slavya.send_chat_action(-1001351496983, 'typing')
        time.sleep(4)
        if user['Slavya_respect'] < 85:
            slavya.send_message(-1001351496983, 'Ладно, спрошу кого-нибудь другого.', reply_to_message_id=m.message_id)
        else:
            slavya.send_message(-1001351496983, 'Ладно, ничего страшного - спрошу кого-нибудь другого.',
                                reply_to_message_id=m.message_id)
        if user['Slavya_respect'] > 0:
            users.update_one({'id': user['id']}, {'$inc': {'Slavya_respect': -1}})

    if pioner == 'uliana':
        ulianastats['whohelps'] = None
        uliana.send_chat_action(-1001351496983, 'typing')
        time.sleep(4)
        if user['Uliana_respect'] < 85:
            uliana.send_message(-1001351496983, 'Ой, ну и ладно! Найду того, кому интересно!',
                                reply_to_message_id=m.message_id)
        else:
            uliana.send_message(-1001351496983, 'Ладно, как хочешь. Но если появится желание - говори!',
                                reply_to_message_id=m.message_id)
        if user['Uliana_respect'] > 0:
            users.update_one({'id': user['id']}, {'$inc': {'Uliana_respect': -1}})


def randomact():
    t = threading.Timer(random.randint(4900, 18000), randomact)
    t.start()
    global rds
    if rds == True:
        lisst = ['talk_uliana+olgadmitrievna', 'talk_uliana+alisa', 'talk_el+shurik']
        x = random.choice(lisst)
        if x == 'talk_uliana+olgadmitrievna':
            bot.send_chat_action(-1001351496983, 'typing')
            time.sleep(4)
            bot.send_message(-1001351496983, nametopioner('uliana') + ', а ну стой! Ты эти конфеты где взяла?',
                             parse_mode='markdown')
            sendstick(bot, 'CAADAgADtwADgi0zD-9trZ_s35yQAg')
            time.sleep(1)
            uliana.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            uliana.send_message(-1001351496983, 'Какие конфеты?')
            sendstick(uliana, 'CAADAgADHQADgi0zD1aFI93sTseZAg')
            time.sleep(2)
            bot.send_chat_action(-1001351496983, 'typing')
            time.sleep(3)
            bot.send_message(-1001351496983, 'Те, что ты за спиной держишь! Быстро верни их в столовую!')
            time.sleep(1)
            uliana.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            uliana.send_message(-1001351496983, 'Хорошо, Ольга Дмитриевна...')
            sendstick(uliana, 'CAADAgADJQADgi0zD1PW7dDuU5hCAg')
        if x == 'talk_uliana+alisa':
            alisa.send_chat_action(-1001351496983, 'typing')
            time.sleep(3)
            alisa.send_message(-1001351496983, nametopioner('uliana') + ', не боишься, что Ольга Дмитриевна спалит?',
                               parse_mode='markdown')
            time.sleep(1)
            uliana.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            uliana.send_message(-1001351496983, 'Ты о чём?')
            time.sleep(2)
            alisa.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            alisa.send_message(-1001351496983, 'О конфетах, которые ты украла!')
            sendstick(alisa, 'CAADAgADOwADgi0zDzD8ZNZXu5LHAg')
            time.sleep(1)
            uliana.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            uliana.send_message(-1001351496983, 'Да не, не спалит! Я так уже много раз делала!')
            sendstick(uliana, 'CAADAgADKQADgi0zD_inNy0pZyh0Ag')
            time.sleep(2)
            alisa.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            alisa.send_message(-1001351496983, 'Тогда делись!')
            time.sleep(1)
            uliana.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            uliana.send_message(-1001351496983, 'Тогда пошли в домик!')
        if x == 'talk_el+shurik':
            electronic.send_chat_action(-1001351496983, 'typing')
            time.sleep(3)
            electronic.send_message(-1001351496983,
                                    nametopioner('shurik') + ', как думаешь, возможно ли перемещение во времени?',
                                    parse_mode='markdown')
            sendstick(electronic, 'CAADAgAD0wADgi0zD1LBx9yoFTBiAg')
            time.sleep(1)
            shurik.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            shurik.send_message(-1001351496983, 'В теории... Хотя нет, это антинаучно.')
            sendstick(shurik, 'CAADAgAD5QADgi0zDwyDLbq7ZQ4vAg')
            time.sleep(2)
            electronic.send_chat_action(-1001351496983, 'typing')
            time.sleep(2)
            electronic.send_message(-1001351496983,
                                    'А мне вот кажется, что когда-нибудь прогресс дойдёт и до такого...')


checktime()

t = threading.Timer(120, randomhelp)
t.start()


def polling(pollingbot):
    pollingbot.polling(none_stop=True, timeout=600)


t = threading.Timer(120, randomact)
t.start()

if True:
    print('7777')
    users.update_many({}, {'$set': {'working': 0}})
    users.update_many({}, {'$set': {'waitforwork': 0}})
    users.update_many({}, {'$set': {'relaxing': 0}})
    users.update_many({}, {'$set': {'answering': 0}})
    t = threading.Timer(1, polling, args=[uliana])
    t.start()
    uliana.send_message(441399484, 'Я могу принимать сообщения!')
    t = threading.Timer(1, polling, args=[bot])
    t.start()
    t = threading.Timer(1, polling, args=[lena])
    t.start()
    t = threading.Timer(1, polling, args=[electronic])
    t.start()
    t = threading.Timer(1, polling, args=[zhenya])
    t.start()
    t = threading.Timer(1, polling, args=[alisa])
    t.start()
    t = threading.Timer(1, polling, args=[slavya])
    t.start()
    t = threading.Timer(1, polling, args=[miku])
    t.start()
    t = threading.Timer(1, polling, args=[tolik])
    t.start()
    t = threading.Timer(1, polling, args=[shurik])
    t.start()
    t = threading.Timer(1, polling, args=[semen])
    t.start()
    t = threading.Timer(1, polling, args=[pioneer])
    t.start()
    t = threading.Timer(1, polling, args=[world])
    t.start()


@world.message_handler(commands=['addplayer'])
def addplayer(m):
    if m.from_user.id == 441399484:
        pioner = m.text.split(' ')[2]
        user = int(m.text.split(' ')[1])
        thunder.insert_one(createeventuser(user, pioner))
        world.send_message(m.chat.id, 'Юзер добавлен!')


def createeventuser(user, pioner):
    return {
        'id': user,
        'pioner': pioner,
        'choicing': 0,
        'ready': 0,
        'nextfunc': None
    }


@world.message_handler(content_types=['photo'])
def imgg(m):
    world.send_photo(441399484, m.photo[0].file_id, caption=str(m.photo[0].file_id))


@world.message_handler(content_types=['audio'])
def audiohandler(m):
    world.send_audio(441399484, m.audio.file_id)
    world.send_message(441399484, m.audio.file_id)


############################################### ПИОНЕР: НАЧАЛО ##############################################

def pi_sends(user):
    if user != None:
        slt = 3
        long = 5
        pi_user = thunder.find_one({'pioner': 'pioner'})
        se_user = thunder.find_one({'pioner': 'semen'})
        world.send_photo(user['id'], 'AgADAgADhqoxGx3TaEs2RjkBAr60m95HhA8ABLaEkJAkRZsEQy8BAAEC')
        world.send_message(user['id'], 'Меня разбудило громкое завывание сработавшей сигнализации.')
        time.sleep(slt)
        world.send_message(user['id'], '~Чёрт, надо будет убавить громкость рупоров.~')
        time.sleep(slt)
        world.send_message(user['id'], 'Я поднялся с кровати и накинул лежавшую рядом кожаную куртку.')
        time.sleep(slt)
        world.send_message(user['id'], 'Я кинул короткий взгляд на часы.')
        time.sleep(slt)
        world.send_message(user['id'], '~7:30~')
        time.sleep(slt)
        world.send_message(user['id'], '~Кого это принесло с утра пораньше?!~')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Нацепив ботинки, я подошел к столу с пультом управления и нажал на небольшую красную кнопку.')
        time.sleep(slt)
        world.send_message(user['id'], 'Звук сирены тут же прекратился.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Я на ходу подхватил с пола фонарь и направился в черноту тоннеля, захлопнув за собой массивную дверь бомбоубежища.')
        time.sleep(slt)
        world.send_message(user['id'], 'Не прошло и пяти минут, как я уже был на месте.')
        world.send_photo(user['id'], 'AgADAgAD_qsxG9QTYUuEsMnVDPodCSNTOQ8ABFoAASsafFfUD_AiBgABAg')
        time.sleep(slt)
        world.send_message(user['id'],
                           'На первый взгляд это был ничем не примечательный свод тоннеля недалеко от входа в катакомбы, однако, ' +
                           'если приглядеться чуть внимательнее, то можно заметить слабо мигающую красную лампочку в самой верхней точки каменного свода.')
        time.sleep(long)
        world.send_message(user['id'],
                           'Именно от этой красной лампочки, вниз, тянулась едва ли заметная леска. В черноте тоннеля заметить её было практически невозможно.')
        time.sleep(slt)
        world.send_message(user['id'], 'Я медленно провёл светом фонаря от потолка до пола тоннеля.')
        time.sleep(slt)
        world.send_message(user['id'], 'Ничего. Леска пропала.')
        time.sleep(slt)
        world.send_message(user['id'], 'Механизм был устоен так, чтобы порвать леску смог только человек.')
        time.sleep(slt)
        world.send_message(user['id'], 'От массы менее пятнадцати килограмм леска бы не порвалась.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Это сразу ликвидировало вариант с лесной живностью. Белка или кролик не смогли бы порвать леску, а сигнализация бы не сработала.')
        time.sleep(long)
        world.send_message(user['id'], 'А это значит, что...')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nДавно не виделись.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Раздался за спиной знакомый голос.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я медленно развернулся и посветил фонарём на источник звука.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Мда. Я ошибся. Лесная живность все-таки смогла порвать леску.~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Передо мной стояла Юля.', parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADkwADgi0zD6BnrLMAAVO12AI')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Пионер_:\nВот так встреча. Кажется, последний раз мы не очень весело расстались.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Юля нервно дёрнула ушами.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Юля_:\nТы сам в этом виноват. Если бы ты сделал правильный выбор, то уехал бы вместе с ним.',
                           parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADkwADgi0zD6BnrLMAAVO12AI')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nДа брось, я уже смирился. Давай не будем давить на старые раны.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nЯ пришла сюда не за этим.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Пионер_:\nТак я и знал. Глупо было надеяться, что ты зашла на чай. Которого, кстати, у меня нет...',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Юля переменилась в лице.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nЧай? Что за чай? Никогда о нем не слышала.', parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADowADgi0zDw_IFESsbO6uAg')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nЭто заваренные запасы.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Коротко обьяснил я ей.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nФу! Какая гадость!', parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADkwADgi0zD6BnrLMAAVO12AI')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nМы отошли от темы. Зачем ты пришла?', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Лицо Юли вновь обрело прежнюю серьёзность.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nЧтобы предупредить тебя.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nПредупредить? О чём?', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nНо для начала мне нужно рассказать тебе все, что знаю сама.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'По моей спине пробежал холодок.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nЧто? Что ты имеешь ввиду?', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Юля раздраженно качнула хвостом.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nНе прикидывайся идиотом. Ты прекрасно меня понял.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я стоял открыв рот, не в силах произнести ни слова.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Все секреты лагеря станут моими!~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Юля тем временем медленными шагами начинала приближаться ко мне.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Подойдя совсем близко, она начала обходить меня вокруг.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nИтак, начнём с самого простого. Кто я такая? Ты знаешь?',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nДевочка-кошка.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Выдавил я.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nНет, не все так просто. Я...', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Её слова прервал оглушительный взрыв где-то на поверхности.',
                           parse_mode='markdown')
        world.send_photo(user['id'], 'AgADAgADh6oxGx3TaEtrkrCzsJYzIotbOQ8ABO6maOEKrBrV7hkGAAEC')
        world.send_audio(user['id'], 'CQADAgADkgMAApS8aEtZQAEN-2XZgwI')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Юля отпрыгнула от меня и оскалилась, посмотрев вверх. Её зрачки превратились в две узкие щелки.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nО нет, я опоздала!', parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADpwADgi0zD3TCQLMRiwEvAg')
        time.sleep(slt)
        world.send_message(user['id'], 'Она резко перевела взгляд на меня.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nУ нас мало времени! Слушай меня, и запоминай!', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Юля_:\nЧерез несколько минут тебя закинет на новую смену. В ней будет много других твоих двойников. Но лишь один из них настоящий. Все остальные не больше чем клоны.',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], '_Юля_:\nГоворю сразу, в лагере будут происходить необьяснимые вещи.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nИ я хочу, чтобы ты был готов, когда встретишься с ними. Ты...',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Очередной взрыв вновь приглушил её слова...', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Я отошел на шаг назад и прислонился спиной к стене. Юля крепче прижала уши к затылку.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Нас стало разделять всё большее расстояние.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nТы должен найти настоящего Семёна!', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я опешил от её слов.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Настоящего?!~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nНастоящего?! Неужели ты намекаешь на...', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Юля с горечью посмотрела мне в глаза.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nСожалею, но это так.', parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADoQADgi0zD07z3mQumb44Ag')
        time.sleep(slt)
        world.send_message(user['id'], '~НЕ МОЖЕТ БЫТЬ!~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Я не могу быть клоном! Я настоящий! Это *я* настоящий Семён!~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nТы должен спасти его. Только один из вас выберется.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nЗапомни!', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Юля_:\n_Восход окрасит бесконечно темное небо багряной краской, как знак того, сколько крови было пролито ради свободы._',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], 'Чужим голосом произнесла Юля.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '~Спасти его?! Ну уж нет. Я не стану жертвовать своей жизнью ради очередного сопливого Семенчика.~',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], 'В груди начала закипать бешеная злоба.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nСпасти его?! Спасти его?!', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nДа пошла ты! Это я настоящий Семен! Это я живой!',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Юля округлила глаза.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Юля_:\nНет, нет, нет... Даже не думай об этом! Ты не представляешь, что тогда произойдет!',
                           parse_mode='markdown')
        world.send_sticker(user['id'], 'CAADAgADnQADgi0zD35x6NCuNd5VAg')
        time.sleep(slt)
        world.send_message(user['id'], 'Я безумно улыбнулся.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nНеужели ты не понимаешь?! Мне нечего терять!', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '_Пионер_:\nТы совершила ошибку, придя сюда. Но я не могу не выразить благодарность тебе за информацию. К сожалению, теперь я буду обладать ей один.',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'],
                           'В этот момент рука уже находилась за спиной. Холодное лезвие упиралось в ремень шорт.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я резко сорвался с места и кинулся на Юлю.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Она вскрикнула.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я рывком вынул нож из тела, кинул девушку на пол и направился к выходу наружу.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Юля_:\nСемен, ты... Совершаешь... Ошибку...', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Прохрипела за спиной Юля.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nНет, ошибку совершили вы, когда отправили меня в этот лагерь.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nНо я выберусь отсюда.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '_Пионер_:\nИ никто меня не остановит...', parse_mode='markdown')
        time.sleep(slt)
        t = threading.Thread(target=se_sends, args=[se_user])
        t.start()
        t = threading.Timer(10, pioner_awaking, args=[pi_user])
        t.start()


############################################### СЕМЁН: НАЧАЛО ##############################################
def se_sends(user):
    if user != None:
        slt = 3
        long = 5
        pi_user = thunder.find_one({'pioner': 'pioner'})
        se_user = thunder.find_one({'pioner': 'semen'})
        world.send_photo(user['id'], '')
        world.send_message(user['id'], 'В глаза ударил яркий свет.')
        time.sleep(slt)
        world.send_message(user['id'], '~Да здраствует новая смена.~')
        time.sleep(slt)
        world.send_message(user['id'], 'Запах бензина и пыли. Вот с чего начинается очередной цикл.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Я машинально встал, и вышел из Икаруса, не забыв захватить пачку "Космоса" из бардачка.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Вокруг все цвело и пахло, как всегда. Прекрасные пейзажи этого мира уже давно перестали удивлять.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Первые смены, бывало даже резали глаза, но человек быстро адаптируется к окружающей среде.')
        time.sleep(long)
        world.send_message(user['id'], 'Я сел на бордюр, подкурил сигарету и принялся ждать.')
        time.sleep(slt)
        world.send_message(user['id'], 'Каждую смену ровно через 15 минут после приезда приходила она.')
        time.sleep(slt)
        world.send_message(user['id'], 'Славя.')
        time.sleep(slt)
        world.send_message(user['id'], 'За время пока я в лагере, я успел неплохо покопаться в себе.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Славя была, пожалуй, единственная, кто ни разу за все циклы не смог мне надоесть.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Она одна кое-как понимала меня, когда я рассказывал ей о моей нелегкой судьбе в этом лагере.')
        time.sleep(slt)
        world.send_message(user['id'], 'Или делала вид?')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Впрочем, неважно, ведь тогда мне было просто необходимо, чтобы меня кто-то выслушал. И она прекрасно исполняла мое желание.')
        time.sleep(long)
        world.send_message(user['id'], 'Я докурил, затушил об асфальт сигарету, и глянул на время.')
        time.sleep(slt)
        world.send_message(user['id'], '10:34.')
        time.sleep(slt)
        world.send_message(user['id'], 'Ну всё, пора идти.')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Подойдя к воротам, я прислушался, приготовясь услышать разговоры двух кибернетиков, как обычно стоявших около клубов.')
        time.sleep(long)
        world.send_message(user['id'], 'Тишина.')
        time.sleep(slt)
        world.send_message(user['id'],
                           '~Странно. Ну ладно. Может при переходе на новый цикл у меня было повреждение слуха.~')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Иногда случались небольшие инциденты при попадании на новую смену. Особенно часто после суицида. Проблемы незначительные, но заметные сразу.')
        time.sleep(long)
        world.send_message(user['id'],
                           'Допустим, я однажды пробовал выпить все таблетки в медпункте, так после пробуждения в автобусе у меня всю смену без причины болел живот.',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], 'Посмотрев еще раз на часы, я обнаружил, что время уже...',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '10:36', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Сердце упало в пятки.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Не может быть!~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я забежал за лагерные ворота.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Насколько же я был удивлен, когда не увидел за воротами НИКОГО!',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Что тут мать твою происходит?!~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Ни одной смены с похожим сюжетом на моей памяти не было.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Всегда в 10:35 Славя приходила меня встречать. Всегда около клубов стояли и разговаривали кибернетики.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Сейчас же меня никто не встретил и около клубов было пусто.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '~Так. Надо собраться. Может быть стоит пройтись по лагерю? Или стоит пойти умыться и придти в себя?~',
                           parse_mode='markdown')
        time.sleep(slt)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Обойти лагерь', callback_data='semen_check_all'))
        kb.add(types.InlineKeyboardButton(text='Пойти к умывальникам', callback_data='semen_goto_wash'))
        world.send_message(user['id'], 'Как поступить?', reply_markup=kb)
        thunder.update_one({'id': user['id']}, {'$set': {'choicing': 1}})


############################################### ПИОНЕР: ПРОБУЖДЕНИЕ ##############################################

def pioner_awaking(user):
    if user != None:
        slt = 3
        long = 5
        pi_user = thunder.find_one({'pioner': 'pioner'})
        world.send_photo(user['id'], '')
        world.send_message(user['id'], 'Я очнулся в бункере, на холодном полу.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Не в автобусе?~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Мне это показалось странным, но потом я вспомнил, что сказала мне Юля в прошлой смене.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '~В лагере будут происходить странные вещи. Эта смена будет последней для всех. И выберется только один...~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           '~Не зря я столько времени готовился к этому! Моё тело значительно сильнее и выносливее всех остальных Семёнов.~',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], 'Я оглядел себя, и злобно ухмыльнулся.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Настало время выбраться отсюда. И я сделаю это, чего бы мне это не стоило.~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я встал с пола, покопался в ящиках и достал оттуда кухонный нож.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Да начнётся игра... *На выживание!*', parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], '...', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я решил выйти наружу через старый корпус.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'По пути я встретил одного из Семенов, о которых мне говорила Юля. Не составило труда избавиться от конкурента, учитывая тот факт, что у меня было оружие.',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'],
                           'Я ещё много раз встречал их копии, и всегда исход был одним. Они физически не способны противостоять мне. Некоторые из них даже первми пытались кидаться на меня.',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], '~Видимо, не одному мне известно о том, что эта смена последняя.~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Интересно, был ли среди них "настоящий", как назвала его Юля?~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'От этой мысли злоба ещё сильнее разгоралась во мне. Мне не хотелось верить в её слова, но подсознательно я понимал, что она права. Ей не было смысла врать мне тогда.',
                           parse_mode='markdown')
        time.sleep(long)
        world.send_message(user['id'], '~Плевать. Выберусь отсюда только я.~', parse_mode='markdown')
        time.sleep(slt)
        thunder.update_one({'pioner': 'pioner'}, {'$set': {'nextfunc': 'pioner_gooutbunker', 'ready': 1}})


############################################### СЛАВЯ: ПРОБУЖДЕНИЕ ##############################################

def slavya_awaking(user):
    if user != None:
        slt = 3
        long = 5
        sl_user = thunder.find_one({'pioner': 'slavya'})
        world.send_photo(user['id'], '')
        world.send_message(user['id'], 'Я как обычно проснулась у себя в домике.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Но Жени тут почему-то не было.', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Странно... Обычно я просыпаюсь раньше неё.~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Ладно. Наверное, она пошла в библиотеку.~', parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Я встала с кровати, оделась, и взяв умывальные принадлежности, отправилась приводить себя в порядок.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Пока я шла к умывальникам, я не встретила ни одного человека.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], '~Где все? Неужели сегодня абсолютно весь лагерь решил проспать линейку?~',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Хотя до линейки было еще где-то пол часа, в это время обычно многие просыпаются и идут по своим делам.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'], 'Я закончила умываться, но обстановка в лагере не давала покоя.',
                           parse_mode='markdown')
        time.sleep(slt)
        world.send_message(user['id'],
                           'Очень странно. Может, стоит спросить Ольгу Дмитриевну? Или пойти в библиотеку и поговорить с Женей?',
                           parse_mode='markdown')
        time.sleep(slt)
        thunder.update_one({'pioner': 'slavya'}, {'$set': {'choicing': 1}})
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Пойти к Ольге Дмитриевне в домик', callback_data='slavya_check_olga'))
        kb.add(types.InlineKeyboardButton(text='Пойти в библиотеку', callback_data='slavya_check_library'))
        world.send_message(user['id'], 'Как поступить?', reply_markup=kb)


def semen_checkall(user):
    pass


@world.callback_query_handler(func=lambda call: True)
def inline(call):
    user = thunder.find_one({'id': call.from_user.id})
    if call.data == 'semen_check_all':
        if user['choicing'] == 1:
            thunder.update_one({'id': call.from_user.id},
                               {'$set': {'choicing': 0, 'nextfunc': 'semen_checkall', 'ready': 1}})
            thunder_variables.update_one({'name': 'semen_checkall'}, {'$set': {'value': 1}})
            checkall()


def checkall():
    no = 0
    for ids in thunder.find({}):
        if ids['ready'] == 0:
            no = 1
    if no == 0:
        for ids in thunder.find({}):
            dofunc(ids)
        thunder.update_many({}, {'$set': {'nextfunc': None, 'ready': 0}})


def dofunc(user):
    if user['nextfunc'] == 'semen_checkall':
        semen_checkall(user)


@world.message_handler(commands=['remove_event_users'])
def delusersevent(m):
    for ids in thunder.find({}):
        thunder.remove({'id': ids['id']})
    world.send_message(m.chat.id, 'success')


#@world.message_handler(commands=['start_event'])
#def starteventt(m):
#    if m.from_user.id == 441399484:
#        for ids in thunder_variables.find({}):
#            thunder_variables.remove({'name': ids['name']})
#        thunder_variables.insert_one(createvar('semen_1choice', None))
#        event_thunder_in_paradise()
#        if len(m.text.split()) == 2:
#            try:
#                event_thunder_in_paradise(polunin_pidor=True)
#            except:
#                bot.send_message(mainchat, 'Полунин облажался')
#                world.send_message(mainchat, traceback.format_exc())
#

#def createvar(name, value):
#    return {
#        'name': name,
#        'value': value
#    }
#

#from events import Event  # этот импорт должен быть тут, чтобы избежать ошибок
#from events.scenaries import grom  # как и этот


#def event_thunder_in_paradise(polunin_pidor=False):
#    actives = ['semen', 'pioner', '']
#    pi_user = thunder.find_one({'pioner': 'pioner'})
#    se_user = thunder.find_one({'pioner': 'semen'})
#    if polunin_pidor:
#        event = Event(mainchat, grom)
#        event.add_user(pi_user['id'], 'pioner')
#        event.add_user(se_user['id'], 'semen')
#        return
#    t = threading.Thread(target=pi_sends, args=[pi_user])
#    t.start()
#    for ids in thunder.find({}):
#        if ids['pioner'] != 'pioner':
#            world.send_message(ids['id'], 'Ваш временной промежуток ещё не настал. Ожидайте, история началась...')
#
