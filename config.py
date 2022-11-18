from aiogram import Bot, Dispatcher
from db import DB
bot = Bot("5452048104:AAFzrvN_LssXCArh1Qy5AaA76DERbxQ5zn8") #вставить свой токен, который можно получить тут: https://t.me/BotFather
db = DB() #экземпляр базы данных
dp = Dispatcher(bot)
