from aiogram import Bot, Dispatcher
from db import DB
bot = Bot("") #вставить свой токен, который можно получить тут: https://t.me/BotFather
db = DB() #экземпляр базы данных
dp = Dispatcher(bot)
