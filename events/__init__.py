from bot import (
    world
)
import time
from telebot.apihelper import ApiException
import random
import threading


class Event:
    def __init__(self, main_chat, scenariy, pause=2):
        self.pause = pause
        self.users = {}
        self.users['main_chat'] = main_chat
        self.scenariy = scenariy
        self.send = {'sticker': self.send_sticker, 'photo': self.send_photo}
        self.now_big_chapter = 0
        self.end_paralels = 0
        self.max_paralells = None

    def add_user(self, id, role):
        if role not in self.users and id not in self.users.values():
            self.users[role] = id
            return True
        return False

    def start(self):
        if self.now_big_chapter == 0:
            self.next_big_chapter()
            return True
        return False

    def next_big_chapter(self):
        self.end_paralels = 0
        self.max_paralells = len(self.scenariy['chapters'][self.now_big_chapter])
        for parallel in self.scenariy['chapters'][self.now_big_chapter]:
            threading.Thread(target=self.send_chapters, args=[parallel])
        self.now_big_chapter += 1

    def send_chapters(self, chapters):
        for chapter in chapters:
            if len(chapter) == 4:
                self.send[chapter[3]](*chapter[:3])
            self.send_message(*chapter)
            # тут будет потом для выборов отдельно
        self.end_paralels += 1
        if self.end_paralels == self.max_paralells:
            self.next_big_chapter()

    def send_message(self, from_bot, target, text):
        from_bot.send_chat_action(self.users[target], 'typing')
        time.sleep(random.uniform(1.5, 3.5))
        try:
            from_bot.send_message(self.users[target], text, parse_mode='Markdown', disable_web_page_preview=True)
        except ApiException:
            from_bot.send_message(self.users[target], text)
        time.sleep(self.pause + len(text)/20)

    def send_sticker(self, from_bot, target, sticker):
        from_bot.send_sticker(self.users[target], sticker)

    def send_photo(self, from_bot, target, photo):
        from_bot.send_photo(self.users[target], photo)
