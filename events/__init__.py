from bot import (
    world
)
import time
from telebot.apihelper import ApiException
import random


class Event:
    def __init__(self, main_chat, scenariy, pause=2):
        self.pause = pause
        self.users = {}
        self.users['main_chat'] = main_chat
        self.scenariy = scenariy

    def add_user(self, id, role):
        if role not in self.users and id not in self.users.values():
            self.users[role] = id
            return True
        return False

    def start(self):
        for chapter in self.scenariy:
            self.send_message(*chapter)
            # тут будет потом для выборов отдельно

    def send_message(self, from_bot, target, text):
        # посылки изображений и аудио пока нет
        from_bot.send_chat_action(self.users[target], 'typing')
        time.sleep(random.uniform(1.5, 3.5))
        try:
            from_bot.send_message(self.users[target], text, parse_mode='Markdown', disable_web_page_preview=True)
        except ApiException:
            from_bot.send_message(self.users[target], text)
        time.sleep(self.pause + len(text)/20)
